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

    def test_profile_structure(self):
        readme = (ROOT / "README.md").read_text()
        for app in ("Markdown Previewer", "JSON Assistant", "Jira Assistant"):
            with self.subTest(app=app):
                self.assertRegex(readme, rf"\[{app}\]\(https://[^)]+\)")
        for label in ("Engineering", "Open source", "Apps"):
            self.assertIn(label, readme)
        self.assertIn("https://www.lalitmee.com", readme)
        self.assertIn("<picture>", readme)
        self.assertIn("https://raw.githubusercontent.com/lalitmee/lalitmee/output/github-contribution-grid-snake.svg", readme)
        self.assertIn("https://raw.githubusercontent.com/lalitmee/lalitmee/output/github-contribution-grid-snake-dark.svg", readme)
        self.assertIn('alt="Animated snake tracing Lalit\'s GitHub contributions"', readme)

    def test_no_stale_or_generated_content(self):
        readme = (ROOT / "README.md").read_text()
        for stale in (
            "https://lalitmee.github.io/portfolio", "2024 Goals",
            "<!--START_SECTION:activity-->", "github-readme-stats.vercel.app",
            "quotes-github-readme.vercel.app", "komarev.com/ghpvc", "header.png",
        ):
            with self.subTest(stale=stale):
                self.assertNotIn(stale, readme)
        for workflow in ("update-readme.yml", "update-stats.yml"):
            self.assertFalse((ROOT / ".github/workflows" / workflow).exists())


if __name__ == "__main__":
    unittest.main()
