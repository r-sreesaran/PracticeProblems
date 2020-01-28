import unittest

from pythonSolution.algorithms.dynamicProgramming.src.LadderClimbing import probhelper


class LadderClimberTest(unittest.TestCase):

   def test1(self):
        self.assertIs(probhelper(3), 3)
   def test2(self):
        self.assertIs(probhelper(5), 2)


if __name__ == '__main__':
    unittest.main()