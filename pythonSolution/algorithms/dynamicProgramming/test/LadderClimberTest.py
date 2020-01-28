import unittest

from pythonSolution.algorithms.dynamicProgramming.src.LadderClimbing import prob


class LadderClimberTest(unittest.TestCase):

   def test1(self):
        self.assertIs(prob(3), 3)
   def test2(self):
        self.assertIs(prob(5), 8)


if __name__ == '__main__':
    unittest.main()