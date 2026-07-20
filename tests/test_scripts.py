import importlib.util
import hashlib
import json
from pathlib import Path
import sys
import unittest
import zipfile
import re
from urllib.parse import unquote


REPO_ROOT = Path(__file__).resolve().parents[1]
ROOT = Path(__file__).resolve().parents[1] / "canopyops"
SCRIPTS = ROOT / "scripts"
VERSION = "0.1.5"
sys.path.insert(0, str(SCRIPTS))
from build_release_manifest import canonical_bytes


def load(name):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class CalculationTests(unittest.TestCase):
    def test_vpd_uses_leaf_temperature(self):
        vpd = load("calculate_vpd")
        cooler = vpd.calculate_vpd(25, 60, 23)["leaf_vpd_kpa"]
        equal = vpd.calculate_vpd(25, 60, 25)["leaf_vpd_kpa"]
        self.assertLess(cooler, equal)
        self.assertAlmostEqual(equal, 1.2671, places=3)

    def test_vpd_rejects_bad_rh(self):
        with self.assertRaises(ValueError):
            load("calculate_vpd").calculate_vpd(25, 101, 25)

    def test_dli(self):
        self.assertAlmostEqual(load("calculate_dli").calculate_dli(500, 12), 21.6)

    def test_irrigation(self):
        result = load("calculate_irrigation").calculate(100, 20, 200, 5)
        self.assertEqual(result["drainage_percent"], 20)
        self.assertEqual(result["delivered_ml_per_plant_per_event"], 100)

    def test_unit_normalization(self):
        normalize = load("normalize_units").normalize
        self.assertAlmostEqual(normalize(77, "f", "c"), 25)
        self.assertAlmostEqual(normalize(1, "us_gal", "l"), 3.785411784)


class RecordTests(unittest.TestCase):
    def test_valid_crop_plan(self):
        validator = load("validate_record")
        schema = json.loads((ROOT / "schemas" / "crop-plan.schema.json").read_text(encoding="utf-8"))
        record = json.loads((Path(__file__).parent / "fixtures" / "valid-crop-plan.json").read_text(encoding="utf-8"))
        self.assertEqual(validator.validate(record, schema), [])

    def test_invalid_crop_plan(self):
        validator = load("validate_record")
        schema = json.loads((ROOT / "schemas" / "crop-plan.schema.json").read_text(encoding="utf-8"))
        errors = validator.validate({"plan_id": "only-one-field"}, schema)
        self.assertTrue(any("missing required property" in error for error in errors))

    def test_plan_lint(self):
        linter = load("lint_cultivation_plan")
        text = (ROOT / "assets" / "crop-plan.md").read_text(encoding="utf-8")
        self.assertEqual(linter.lint_markdown(text), [])

    def test_freshness(self):
        from datetime import date

        checker = load("check_source_freshness")
        results = checker.check([{"identifier": "x", "accessed_at": "2026-01-01"}], date(2026, 2, 15), 30)
        self.assertEqual(results[0]["status"], "review-due")

    def test_log_normalization_requires_timezone(self):
        normalizer = load("normalize_logs")
        with self.assertRaises(ValueError):
            normalizer.iso_timestamp("2026-01-01T10:00:00")
        row = normalizer.normalize_row({"datetime": "2026-01-01T10:00:00-06:00", "temp_f": "77", "rh": "60"})
        self.assertEqual(row["temperature_c"], "25.0000")
        self.assertEqual(row["timestamp"], "2026-01-01T16:00:00Z")


class PackageTests(unittest.TestCase):
    def test_required_surfaces_exist(self):
        for relative in [
            "SKILL.md",
            "personas/ella-greenfield-v2.md",
            "evals/eval-manifest.yaml",
            "workflows/review-and-release.md",
        ]:
            self.assertTrue((ROOT / relative).is_file(), relative)

    def test_all_json_schemas_parse(self):
        for path in (ROOT / "schemas").glob("*.json"):
            json.loads(path.read_text(encoding="utf-8"))

    def test_version_custody(self):
        plugin = json.loads((REPO_ROOT / "plugins" / "canopyops" / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
        self.assertEqual(plugin["version"], VERSION)
        for name in ["eval-manifest.yaml", "core-transfer-cases.yaml", "authority-and-resilience-cases.yaml"]:
            document = json.loads((ROOT / "evals" / name).read_text(encoding="utf-8"))
            self.assertEqual(document["package_version"], VERSION, name)
        for name in ["README.md", "INSTALL.md", "DATA-AND-PRIVACY.md", "FAQ.md", "SECURITY.md", "RELEASE-NOTES-v0.1.5.md"]:
            self.assertIn("v0.1.5", (REPO_ROOT / name).read_text(encoding="utf-8"), name)
        self.assertEqual("./assets/canopyops-icon-v0.1.5.png", plugin["interface"]["composerIcon"])
        self.assertTrue((REPO_ROOT / "plugins" / "canopyops" / "assets" / "canopyops-icon-v0.1.5.png").is_file())

    def test_plugin_skill_matches_canonical_tree(self):
        plugin_root = REPO_ROOT / "plugins" / "canopyops" / "skills" / "canopyops"
        canonical = {path.relative_to(ROOT).as_posix(): path.read_bytes() for path in ROOT.rglob("*") if path.is_file() and "__pycache__" not in path.parts}
        plugin = {path.relative_to(plugin_root).as_posix(): path.read_bytes() for path in plugin_root.rglob("*") if path.is_file() and "__pycache__" not in path.parts}
        self.assertEqual(plugin, canonical)

    def test_claude_archive_matches_canonical_tree(self):
        archive_path = REPO_ROOT / "claude-ai" / f"canopyops-v{VERSION}.zip"
        canonical = {f"canopyops/{path.relative_to(ROOT).as_posix()}": canonical_bytes(path) for path in ROOT.rglob("*") if path.is_file() and "__pycache__" not in path.parts}
        with zipfile.ZipFile(archive_path) as archive:
            archived = {name: archive.read(name) for name in archive.namelist() if not name.endswith("/")}
        self.assertEqual(archived, canonical)
        self.assertEqual({name.split("/", 1)[0] for name in archived}, {"canopyops"})

    def test_release_manifest_hashes_and_inventory(self):
        manifest_path = REPO_ROOT / "release-manifest.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        self.assertEqual(manifest["version"], VERSION)
        recorded = {item["path"]: item for item in manifest["files"]}
        current = {
            path.relative_to(REPO_ROOT).as_posix(): path
            for path in REPO_ROOT.rglob("*")
            if path.is_file()
            and not any(part in {".git", "__pycache__", ".pytest_cache", "release-assets"} for part in path.parts)
            and path.name != "release-manifest.json"
        }
        self.assertEqual(set(recorded), set(current))
        for relative, path in current.items():
            data = canonical_bytes(path)
            self.assertEqual(recorded[relative]["bytes"], len(data), relative)
            self.assertEqual(recorded[relative]["sha256"], hashlib.sha256(data).hexdigest(), relative)

    def test_customer_document_manifest_and_local_links(self):
        manifest = json.loads((REPO_ROOT / "documentation-manifest.json").read_text(encoding="utf-8"))
        documents = manifest["customer_docs"]
        self.assertEqual(21, len(documents))
        self.assertEqual(len(documents), len(set(documents)))
        declared = set(documents)
        for paths in manifest["moments"].values():
            self.assertTrue(paths)
            self.assertTrue(set(paths).issubset(declared))
        broken = []
        pattern = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
        for relative in documents:
            source = REPO_ROOT / relative
            self.assertTrue(source.is_file(), relative)
            for raw in pattern.findall(source.read_text(encoding="utf-8")):
                target = raw.strip().split("#", 1)[0].strip(" <>")
                if not target or target.startswith(("http://", "https://", "mailto:", "tel:", "data:")):
                    continue
                resolved = (source.parent / unquote(target)).resolve()
                if not resolved.exists():
                    broken.append(f"{relative} -> {raw}")
        self.assertEqual([], broken)


if __name__ == "__main__":
    unittest.main()
