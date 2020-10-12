import unittest

from Solutions.codechef.DSALearningSeries.complexityAnalysisAndWarmup import MULTHREE

from Solutions.codechef.DSALearningSeries.complexityAnalysisAndWarmup import multhreeAlternative


class MyTestCase(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(MULTHREE.multiple(20,1,1), multhreeAlternative.multiple1(20,1,1))

    def test_case2(self):
        self.assertEqual(MULTHREE.multiple(20,1,2), multhreeAlternative.multiple1(20,1,2))

    def test_case3(self):
        self.assertEqual(MULTHREE.multiple(20,2,1), multhreeAlternative.multiple1(20,2,1))

    def test_case4(self):
        self.assertEqual(MULTHREE.multiple(20,2,3), multhreeAlternative.multiple1(20,2,3))

    def test_case5(self):
        self.assertEqual(MULTHREE.multiple(20,2,5), multhreeAlternative.multiple1(20,2,5))

    def test_case6(self):
        self.assertEqual(MULTHREE.multiple(20,5,5), multhreeAlternative.multiple1(20,5,5))


if __name__ == '__main__':
    unittest.main()
