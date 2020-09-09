import unittest

from pythonSolution.misc.solutions.palindromeWordChecker import checkStringIsPalindrome

class CheckPalindromeWordChecker(unittest.TestCase):
    def test1(self):
        string = "isa si"
        self.assertTrue(checkStringIsPalindrome(string))

