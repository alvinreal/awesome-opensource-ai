import tempfile
import unittest
from pathlib import Path

import validate_awesome


class ValidateAwesomeTests(unittest.TestCase):
    def parse_entries(self, lines: list[str]):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "README.md"
            path.write_text("\n".join(lines), encoding="utf-8")
            return validate_awesome.parse_entries(path)

    def test_reports_malformed_github_entry(self):
        entries, problems = self.parse_entries(
            ["- [Broken](https://github.com/acme/broken - Description."]
        )

        self.assertEqual(entries, [])
        self.assertEqual([problem.severity for problem in problems], ["error"])
        self.assertEqual(
            problems[0].message, "entry link markup could not be parsed"
        )

    def test_allows_star_badge_in_entry_description(self):
        entries, problems = self.parse_entries(
            [
                "- [Project](https://github.com/acme/project) - Description. "
                "![GitHub stars](https://img.shields.io/github/stars/acme/project?style=social)"
            ]
        )

        self.assertEqual(len(entries), 1)
        self.assertEqual(problems, [])

    def test_reports_project_link_after_description(self):
        _, problems = self.parse_entries(
            [
                "- [One](https://github.com/acme/one) - Description. "
                "![GitHub stars](https://img.shields.io/github/stars/acme/one?style=social) "
                "+ **[Two](https://github.com/acme/two)** "
                "![GitHub stars](https://img.shields.io/github/stars/acme/two?style=social)"
            ]
        )

        self.assertEqual([problem.severity for problem in problems], ["error"])
        self.assertEqual(
            problems[0].message,
            "entry contains a project link after its description",
        )

    def test_reports_duplicate_repository_across_sections(self):
        entries, problems = self.parse_entries(
            [
                "## First",
                "- [Project](https://github.com/acme/project) - Description. "
                "![GitHub stars](https://img.shields.io/github/stars/acme/project?style=social)",
                "## Second",
                "- [Project again](https://github.com/acme/project/) - Description. "
                "![GitHub stars](https://img.shields.io/github/stars/acme/project?style=social)",
            ]
        )

        duplicate_problems = validate_awesome.validate_duplicates(entries)

        self.assertEqual(problems, [])
        self.assertEqual(
            [problem.severity for problem in duplicate_problems], ["warning"]
        )
        self.assertIn(
            "repo `acme/project` appears multiple times",
            duplicate_problems[0].message,
        )


if __name__ == "__main__":
    unittest.main()
