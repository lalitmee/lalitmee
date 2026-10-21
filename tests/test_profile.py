import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ProfileTests(unittest.TestCase):
    def test_snake_workflow(self):
        workflow = (ROOT / ".github/workflows/contribution-snake.yml").read_text()
        self.assertIn("Platane/snk/svg-only@v3", workflow)
        self.assertIn("outputs: |", workflow)
        self.assertIn("dist/github-contribution-grid-snake.svg\n", workflow)
        self.assertIn("dist/github-contribution-grid-snake-dark.svg?palette=github-dark", workflow)
        self.assertIn("target_branch: output", workflow)
        self.assertIn("build_dir: dist", workflow)
        self.assertIn("contents: write", workflow)
        self.assertNotIn("svg_out_path:", workflow)


if __name__ == "__main__":
    unittest.main()
