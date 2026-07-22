import unittest

from get_tabs_tool import parse_tab_line


class ParseTabLineTests(unittest.TestCase):
    def test_parses_title_and_url(self):
        self.assertEqual(
            parse_tab_line("Example|||https://example.com/"),
            {"title": "Example", "url": "https://example.com/"},
        )

    def test_preserves_delimiter_inside_url(self):
        self.assertEqual(
            parse_tab_line("Example|||https://example.com/a|||b"),
            {"title": "Example", "url": "https://example.com/a|||b"},
        )

    def test_ignores_unrecognized_lines(self):
        self.assertIsNone(parse_tab_line("not a tab record"))


if __name__ == "__main__":
    unittest.main()
