from unittest import TestCase, main
import importlib

p9095 = importlib.import_module("9095")

class Testclass(TestCase):
    testcase = [
            (1, 1),
            (2, 2),
            (3, 4),
            (4, 7),
            (5, 13),
            (6, 24),
            (7, 44),
            (10, 274),
        ]

    def test9095(self):
        for n, answer in Testclass.testcase:
            self.assertEqual(p9095.testcode(n), answer)

    def testsolution2(self):
        for n, answer in Testclass.testcase:
            self.assertEqual(p9095.solution2(n), answer)

if __name__=="__main__":
    main()