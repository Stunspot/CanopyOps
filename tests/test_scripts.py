import hashlib
import importlib.util
import json
from pathlib import Path
import re
import sys
import unittest
from urllib.parse import unquote
import zipfile


REPO_ROOT = Path(__file__).resolve().parents[1]
ROOT = REPO_ROOT / "canopyops"
SCRIPTS = ROOT / "scripts"
SOURCE_VERSION = "0.1.5"
PORTABLE_VERSION = "0.1.6"
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

    def test_repository_native_version_custody(self):
        plugin = json.loads((REPO_ROOT / "plugins" / "canopyops" / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
        self.assertEqual(plugin["version"], SOURCE_VERSION)
        for name in ["eval-manifest.yaml", "core-transfer-cases.yaml", "authority-and-resilience-cases.yaml"]:
            document = json.loads((ROOT / "evals" / name).read_text(encoding="utf-8"))
            self.assertEqual(document["package_version"], SOURCE_VERSION, name)
        self.assertEqual("./assets/canopyops-icon-v0.1.5.png", plugin["interface"]["composerIcon"])
        self.assertTrue((REPO_ROOT / "plugins" / "canopyops" / "assets" / "canopyops-icon-v0.1.5.png").is_file())

    def test_portable_release_custody(self):
        portable_root = REPO_ROOT / "releases" / f"v{PORTABLE_VERSION}"
        manifest = json.loads((portable_root / "manifest.json").read_text(encoding="utf-8"))
        receipt = json.loads((portable_root / "receipt.json").read_text(encoding="utf-8"))
        plugin = json.loads((portable_root / "codex" / "canopyops" / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["family"]["version"], PORTABLE_VERSION)
        self.assertEqual(receipt["version"], PORTABLE_VERSION)
        self.assertEqual(plugin["version"], PORTABLE_VERSION)
        self.assertTrue((portable_root / f"CanopyOps-v{PORTABLE_VERSION}.zip").is_file())
        self.assertTrue((portable_root / f"CanopyOps-v{PORTABLE_VERSION}.zip.sha256").is_file())
        self.assertTrue((portable_root / "docs" / "VALIDATION.md").is_file())

    def test_plugin_skill_matches_canonical_tree(self):
        plugin_root = REPO_ROOT / "plugins" / "canopyops" / "skills" / "canopyops"
        canonical = {
            path.relative_to(ROOT).as_posix(): path.read_bytes()
            for path in ROOT.rglob("*")
            if path.is_file() and "__pycache__" not in path.parts
        }
        plugin = {
            path.relative_to(plugin_root).as_posix(): path.read_bytes()
            for path in plugin_root.rglob("*")
            if path.is_file() and "__pycache__" not in path.parts
        }
        self.assertEqual(plugin, canonical)

    def test_claude_archive_matches_canonical_tree(self):
        archive_path = REPO_ROOT / "claude-ai" / f"canopyops-v{SOURCE_VERSION}.zip"
        canonical = {
            f"canopyops/{path.relative_to(ROOT).as_posix()}": canonical_bytes(path)
            for path in ROOT.rglob("*")
            if path.is_file() and "__pycache__" not in path.parts
        }
        with zipfile.ZipFile(archive_path) as archive:
            archived = {name: archive.read(name) for name in archive.namelist() if not name.endswith("/")}
        self.assertEqual(archived, canonical)
        self.assertEqual({name.split("/", 1)[0] for name in archived}, {"canopyops"})

    def test_release_manifest_routes_to_scoped_custody(self):
        pointer = json.loads((REPO_ROOT / "release-manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(pointer["format"], "cd-release-manifest-pointer/v1")
        self.assertEqual(pointer["repository_native_line"], SOURCE_VERSION)
        self.assertEqual(pointer["portable_line"], PORTABLE_VERSION)

        historical_path = REPO_ROOT / pointer["historical_repository_snapshot"]
        historical = json.loads(historical_path.read_text(encoding="utf-8"))
        self.assertEqual(historical["format"], "cd-public-release-manifest/v1")
        self.assertEqual(historical["version"], SOURCE_VERSION)
        self.assertTrue((REPO_ROOT / pointer["v0.1.6_package_manifest"]).is_file())
        self.assertTrue((REPO_ROOT / pointer["current_documentation_manifest"]).is_file())

        custody = (REPO_ROOT / "ARCHIVE-CUSTODY.md").read_text(encoding="utf-8")
        self.assertIn("custody router", custody)
        self.assertIn("not a checksum of current repository HEAD", custody)

    def test_customer_document_manifest_and_local_links(self):
        manifest = json.loads((REPO_ROOT / "documentation-manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["format"], "cd-customer-documentation/v2")
        documents = manifest["customer_docs"]
        self.assertGreaterEqual(len(documents), 23)
        self.assertEqual(len(documents), len(set(documents)))
        declared = set(documents)
        for paths in manifest["moments"].values():
            self.assertTrue(paths)
            self.assertTrue(set(paths).issubset(declared))

        for relative in documents + manifest["maintainer_docs"] + manifest["web_surfaces"]:
            self.assertTrue((REPO_ROOT / relative).exists(), relative)

        broken = []
        pattern = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
        markdown_files = [
            relative
            for relative in documents + manifest["maintainer_docs"]
            if relative.endswith(".md")
        ]
        for relative in markdown_files:
            source = REPO_ROOT / relative
            for raw in pattern.findall(source.read_text(encoding="utf-8")):
                target = raw.strip().split("#", 1)[0].strip(" <>")
                if not target or target.startswith(("http://", "https://", "mailto:", "tel:", "data:")):
                    continue
                resolved = (source.parent / unquote(target)).resolve()
                if not resolved.exists():
                    broken.append(f"{relative} -> {raw}")
        self.assertEqual([], broken)

    def test_public_copy_uses_canonical_release_status(self):
        status = (REPO_ROOT / "RELEASE-STATUS.md").read_text(encoding="utf-8")
        self.assertIn("Repository-native source and plugin", status)
        self.assertIn("Settled portable bundle", status)
        self.assertIn(f"v{SOURCE_VERSION}", status)
        self.assertIn(f"v{PORTABLE_VERSION}", status)

        for name in [
            "README.md",
            "START-HERE.md",
            "INSTALL.md",
            "FAQ.md",
            "DATA-AND-PRIVACY.md",
            "SECURITY.md",
            "SUPPORT.md",
            "ARCHIVE-CUSTODY.md",
        ]:
            self.assertIn("RELEASE-STATUS.md", (REPO_ROOT / name).read_text(encoding="utf-8"), name)

        judge = (REPO_ROOT / "JUDGE-QUICKSTART.md").read_text(encoding="utf-8")
        self.assertIn("Ran 20 tests", judge)
        pages = (REPO_ROOT / "docs" / "index.html").read_text(encoding="utf-8")
        self.assertIn("RELEASE-STATUS.md", pages)
        self.assertIn("DOCUMENTATION-STATUS.md", pages)

    def test_pages_local_assets_and_links(self):
        page = REPO_ROOT / "docs" / "index.html"
        source = page.read_text(encoding="utf-8")
        references = re.findall(r'(?:href|src)="([^"]+)"', source)
        broken = []
        for raw in references:
            if raw.startswith(("#", "http://", "https://", "mailto:", "tel:", "data:")):
                continue
            target = raw.split("#", 1)[0].split("?", 1)[0]
            if not target:
                continue
            resolved = (page.parent / unquote(target)).resolve()
            if not resolved.exists():
                broken.append(raw)
        self.assertEqual([], broken)
        self.assertNotIn(".svg", source.lower())


if __name__ == "__main__":
    unittest.main()
