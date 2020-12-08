import unittest
from INPSTFIX  import  infix_to_postfix


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(infix_to_postfix(1,"((A+B)*D)^(E-F)",15), "AB+D*EF-^")

    def test_something1(self):
        self.assertEqual(infix_to_postfix(1,"A+(B*C-(D/E^F)*G)*H",19), "ABC*DEF^/G*-H*+")

    def test_something2(self):
        self.assertEqual(infix_to_postfix(1,"(A+B)",5), "AB+")

    def test_something3(self):
        self.assertEqual(infix_to_postfix(1,"A+B+C",5), "AB+C+")

    def test_something4(self):
        self.assertEqual(infix_to_postfix(1, "A*B+C", 5), "AB*C+")


    def test_something5(self):
        self.assertEqual(infix_to_postfix(1, "(A+B)*C", 5), "AB+C*")


    def test_something6(self):
        self.assertEqual(infix_to_postfix(1, "(A+B/(D^E))*C", 13), "ABDE^/+C*")

    def test7(self):
        self.assertEqual(infix_to_postfix(1,"((A*B)+(C/D))",13),"AB*CD/+".strip())



    def test9(self):
        self.assertEqual(infix_to_postfix(1,"A+B-C",13),"AB+C-".strip())

if __name__ == '__main__':
    unittest.main()
