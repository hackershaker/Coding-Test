from unittest import TestCase, main
import importlib

p1110 = importlib.import_module("1110")

class BaekjoonTest(TestCase):
    def test1002(self):
        testcase = [
            ("26", "4"),
            ("55", "3")
        ]
        for n, ans in testcase:
            self.assertEqual(p1110.solution(n), ans, f"testcase: {n}")
        return

if __name__=="__main__":
    main()