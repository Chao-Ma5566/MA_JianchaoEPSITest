import unittest
import datetime
from unittest.mock import patch
from test_console import salutation, reverse, check_plalindrome, farewell

class TestGreetings(unittest.TestCase):
    def test_salutation_morning(self):
        with patch('builtins.input', return_value='mock_input'):
            with patch('datetime.datetime.now', return_value=datetime.datetime(2023, 1, 1, 9, 0, 0)):
                self.assertEqual(salutation(), "Bonjour,早上好")

    def test_reverse(self):
        self.assertEqual(reverse("hello"), "olleh")
        self.assertEqual(reverse("python"), "nohtyp")
        self.assertEqual(reverse(""), "")

    def test_check_plalindrome(self):
        self.assertTrue(check_plalindrome("kayak"))
        self.assertEqual(check_plalindrome("A man a plan a canal Panama"))
        self.assertEqual(reverse(""), "")

    def test_farewell_morning(self):
        with patch('datetime.datetime.now', return_value=datetime.datetime(2023, 1, 1, 9, 0, 0)):
            with patch('builtins.print') as mock_print:
                farewell()
                mock_print.assert_called_with("bonné journée, 愉快的一天")

    def test_farewell_evening(self):
        with patch('datetime.datetime.now', return_value=datetime.datetime(2023, 1, 1, 20, 0, 0)):
            with patch('builtins.print') as mock_print:
                farewell()
                mock_print.assert_called_with("bonné soirée, 晚上好")

unittest.main()