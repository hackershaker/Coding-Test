from unittest import TestCase, main
import importlib

p1463 = importlib.import_module("1463")

class Testclass(TestCase):
    def test8958(self):
        testcase = [
            (2,1),
            (3,1),
            (4,2),
            (5,3),
            (6,2),
            (7,3),
            (8,3),
            (9,2),
            (10,3),
            (11,4),
            (12,3),
            (13,4),
            (14,4),
            (15,4),
            (16,4),
            (17,5),
            (18,3),
            (19,4),
            (20,4),
            (21,4),
            (24,4),
            (27,3),
            (28,4),
            (29,5),
            (30,4),
            (31,5),
            (32,5),
            (33,5),
        ]

        for case, answer in testcase:
            self.assertEqual(p1463.solution(case), answer, f"{case}, {answer}")

if __name__=="__main__":
    main()