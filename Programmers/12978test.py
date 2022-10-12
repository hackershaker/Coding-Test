from unittest import TestCase, main
import importlib

p12978 = importlib.import_module("12978")
class Testclass(TestCase):
    def test12978(self):
        testcase = [(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3, 4),
        (6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4, 4),
        (5, [[1, 2, 1], [1, 2, 2], [1, 2, 3], [1, 2, 4], [2, 3, 3], [2, 3, 5], [5, 2, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3, 4),
        (2, [[1, 2, 1], [1, 2, 2], [1, 2, 3], [1, 2, 4], [1, 2, 5]], 3, 2),
        ]

        for n, r, k, ans in testcase:
            self.assertEqual(p12978.solution(n,r,k), ans, f"failed testcase : {n, r, k}")



if __name__=="__main__":
    main()