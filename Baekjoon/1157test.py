from unittest import TestCase, main
import importlib

p8958 = importlib.import_module("1157")

class Testclass(TestCase):
    def test8958(self):
        testcase = [
            ("Mississipi", "?"),
            ("zZa", "Z"),
            ("z", "Z"),
            ("baaa", "A"),
            ("abrabr", "?"),
        ]

        for case, answer in testcase:
            self.assertEqual(p8958.solution(case), answer)

if __name__=="__main__":
    main()