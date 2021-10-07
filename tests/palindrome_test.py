import unittest
from icecream import ic
from basic.palindrome.models import Palindrome


class PalindromeTest(unittest.TestCase):
    mock = Palindrome()

    def test_str_to_list(self):
        ic(self.mock.str_to_list("A man, a plan, a canal : Panama"))

    def test_isPalindrome(self):
        ic(self.mock.isPalindrome(self.mock.str_to_list("A man, a plan, a canal : Panama")))


if __name__ == '__main__':
    unittest.main()

