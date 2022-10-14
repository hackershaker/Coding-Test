from unittest import TestCase, main
import importlib

p8958 = importlib.import_module("8958")

class Testclass(TestCase):
    def test8958(self):
        testcase = [
            ("OOXXOXXOOO", 10),
            ("OOXXOOXXOO", 9),
            ("OXOXOXOXOXOXOX", 7),
            ("OOOOOOOOOO", 55),
            ("OOOOXOOOOXOOOOX", 30),
        ]

        for case, answer in testcase:
            self.assertEqual(p8958.solution(case), answer)

if __name__=="__main__":
    main()