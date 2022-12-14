from functools import cmp_to_key
from unittest import TestCase, main
import importlib

p92342 = importlib.import_module("92342")

class TestClass(TestCase):
    testcase = [
        (3, [2,1,0,0,0,0,0,0,0,0,0], [0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0]),
        (5, [3,1,1,0,0,0,0,0,0,0,0], [0, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0]),
        (5, [2,1,1,1,0,0,0,0,0,0,0], [0, 2, 2, 0, 1, 0, 0, 0, 0, 0, 0]),
        (9, [0,0,1,2,0,1,1,1,1,1,1], [1,1,2,0,1,2,2,0,0,0,0]),
        (8, [1,0,2,0,0,1,1,0,2,1,0], [2, 1, 3, 1, 1, 0, 0, 0, 0, 0, 0]),
        (10, [1,0,0,0,0,0,0,0,4,3,2], [2, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1]),
        (10, [1,0,0,0,0,0,0,1,2,3,3], [2, 1, 1, 1, 1, 1, 1, 2, 0, 0, 0]),
        (10, [1,1,1,1,0,0,0,1,1,1,3], [2, 2, 2, 2, 1, 1, 0, 0, 0, 0, 0]),
        (10, [1,1,1,1,1,1,1,1,1,1,0], [2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0]),
        (10, [1,1,1,1,1,1,1,1,1,0,1], [2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0]),
        (10, [2,0,0,0,2,0,2,0,2,2,2], [3, 1, 1, 1, 3, 1, 0, 0, 0, 0, 0]),
        (10, [2,2,2,0,0,0,0,0,2,2,2], [3, 3, 3, 1, 0, 0, 0, 0, 0, 0, 0]),
        (10, [2,0,2,0,2,0,2,0,2,2,0], [3, 1, 3, 1, 0, 1, 0, 1, 0, 0, 0]),
        (10, [2,0,2,0,2,0,2,0,2,2,0], [3, 1, 3, 1, 0, 1, 0, 1, 0, 0, 0]),
        (10, [3,2,1,0,0,0,0,1,1,2,0], [4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0]),
        (10, [5,3,1,1,0,0,0,0,0,0,0], [0, 4, 2, 2, 1, 1, 0, 0, 0, 0, 0]),
        (1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [-1]),
        (3, [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], [-1]),
        (5, [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0], [2, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0]),
        (4, [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0], [2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
        (4, [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0], [2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]),
        (10, [3, 3, 2, 2, 0, 0, 0, 0, 0, 0, 0], [4, 0, 3, 0, 1, 1, 1, 0, 0, 0, 0]),
        (7, [4, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 4, 1, 1, 1, 0, 0, 0, 0, 0, 0]),
        (4, [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0], [2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
        (10, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0]),
        (10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3], [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 2]),
        (10, [0, 3, 4, 3, 0, 0, 0, 0, 0, 0, 1], [1, 4, 0, 0, 1, 1, 1, 1, 1, 0, 0]),
        (10, [0, 0, 0, 0, 0, 0, 0, 1, 3, 3, 3], [1, 1, 1, 1, 1, 1, 1, 2, 0, 0, 1]),
        (10, [1, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3], [2, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1]),
        (10, [1, 0, 0, 0, 0, 0, 0, 0, 2, 3, 4], [2, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1]),
        (10, [0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 3], [1, 1, 1, 1, 1, 0, 2, 3, 0, 0, 0]),
        (10, [0, 0, 0, 0, 0, 0, 1, 4, 2, 0, 3], [1, 1, 1, 1, 1, 1, 2, 0, 0, 1, 1]),
        (10, [4, 0, 0, 0, 0, 0, 1, 0, 2, 0, 3], [5, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]),
        (10, [2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0], [3, 3, 3, 0, 0, 1, 0, 0, 0, 0, 0]),
        (10, [0, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0], [1, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0]),
        (10, [0, 0, 0, 0, 0, 0, 1, 2, 3, 3, 2], [1, 1, 1, 1, 1, 0, 2, 3, 0, 0, 0]),
        (10, [0, 0, 0, 0, 0, 0, 2, 2, 2, 3, 2], [1, 1, 1, 1, 1, 1, 3, 0, 0, 0, 1]),
        (10, [0, 0, 0, 0, 0, 1, 1, 2, 2, 3, 2], [1, 1, 1, 1, 1, 2, 2, 0, 0, 0, 1]),
        (10, [0, 0, 0, 1, 1, 1, 1, 0, 2, 3, 2], [1, 1, 1, 2, 2, 2, 0, 1, 0, 0, 0]),
        (10, [0, 0, 0, 1, 1, 2, 2, 0, 2, 3, 2], [1, 1, 1, 2, 2, 3, 0, 0, 0, 0, 0]),
        (10, [3, 1, 1, 1, 1, 0, 2, 0, 0, 1, 0], [0, 2, 2, 2, 2, 1, 0, 1, 0, 0, 0]),
        (10, [3, 2, 1, 1, 1, 0, 2, 0, 0, 0, 0], [0, 3, 2, 2, 2, 1, 0, 0, 0, 0, 0]),
        (10, [0, 2, 2, 2, 1, 1, 1, 1, 0, 0, 0], [1, 3, 3, 0, 2, 0, 0, 0, 1, 0, 0]),
    ]

    def test92342(self):
        for n, info, answer in TestClass.testcase:
            self.assertEqual(p92342.solution(n, info), answer, f"n: {n}, info: {info}")

    from functools import cmp_to_key
    def testcompare(self):
        self.assertEqual(sorted([[2, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0], [2, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1]], key=cmp_to_key(p92342.compare)), [[2, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1], [2, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0]])
        self.assertEqual(sorted([[3,2,1], [2,3,1], [1,2,3]], key=cmp_to_key(p92342.compare)), [[1,2,3], [2,3,1], [3,2,1]])
        self.assertEqual(sorted([[3,2,2], [2,3,1], [1,2,2]], key=cmp_to_key(p92342.compare)), [[3,2,2], [1,2,2], [2,3,1]])
        self.assertEqual(sorted([[3,2,2], [2,3,1], [1,2,2]], key=cmp_to_key(p92342.compare)), [[3,2,2], [1,2,2], [2,3,1]])
if __name__=="__main__":
    main()