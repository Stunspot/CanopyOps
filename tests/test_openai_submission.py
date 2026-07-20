import json
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "canopyops"
ARCHIVE = (
    ROOT
    / "release-assets"
    / "v0.1.5"
    / "Plugin-CanopyOps-v0.1.5-OpenAI-Submission.zip"
)
CUSTODY = ROOT / "release-assets" / "v0.1.5" / "openai-submission-custody.json"


class OpenAISubmissionTests(unittest.TestCase):
    def test_submission_archive_is_reproducible_and_portal_shaped(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / ARCHIVE.name
            custody = Path(temporary) / CUSTODY.name
            subprocess.run(
                [
                    sys.executable,
                    str(ROOT / "tools" / "build_openai_submission_archive.py"),
                    str(PLUGIN),
                    "--output",
                    str(output),
                    "--json-output",
                    str(custody),
                ],
                check=True,
                capture_output=True,
                text=True,
            )
            self.assertEqual(ARCHIVE.read_bytes(), output.read_bytes())
            self.assertEqual(
                json.loads(CUSTODY.read_text(encoding="utf-8")),
                json.loads(custody.read_text(encoding="utf-8")),
            )

        with zipfile.ZipFile(ARCHIVE) as archive:
            names = archive.namelist()
            self.assertTrue(names)
            self.assertTrue(all("\\" not in name for name in names))
            manifest = json.loads(
                archive.read("canopyops-plugin/.codex-plugin/plugin.json").decode(
                    "utf-8"
                )
            )
            self.assertEqual({"composerIcon", "logo"}, set(manifest["interface"]))


if __name__ == "__main__":
    unittest.main()
