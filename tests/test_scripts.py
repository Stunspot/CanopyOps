import importlib.util
import json
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1] / "canopyops"
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))


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


if __name__ == "__main__":
    unittest.main()
