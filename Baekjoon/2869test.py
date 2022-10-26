from unittest import TestCase, main
import importlib

p2869 = importlib.import_module("2869")

class testClass(TestCase):
    testcase = [
        (3,1,4, 2),
        (2,1,5, 4),
        (5,1,6, 2),
        (100,99,1000000000, 999999901),
    ]

    def test2869(self):
        for a,b,v,answer in testClass.testcase:
            self.assertEqual(p2869.solution(a,b,v), answer, f"a:{a}, b:{b}, v:{v}, answer: {answer}")

if __name__=="__main__":
    main()