from unittest import TestCase, main
import importlib

p10250 = importlib.import_module("10250")

class Testclass(TestCase):
    def test8958(self):
        testcase = [
            (6, 12, 10, 402),
            (30, 50, 72, 1203),
        ]

        for h, w, n, answer in testcase:
            self.assertEqual(p10250.solution(h, w, n), answer)

if __name__=="__main__":
    main()