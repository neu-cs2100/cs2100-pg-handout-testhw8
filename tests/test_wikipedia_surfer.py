from unittest.mock import patch
import unittest
import sys

sys.path.append(".")
from src.main import WikipediaSurfer


class TestWikipediaPage(unittest.TestCase):
    @patch(
        "builtins.input", return_value="computer"
    )  # temporarily replace input() with a function that returns "computer"
    def test_get_user_name(self, mock_input: unittest.mock.Mock) -> None:
        surfer = WikipediaSurfer("cat")
        self.assertEqual(surfer.current_page.keyword.lower(), "computer")
