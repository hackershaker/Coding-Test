from unittest import TestCase, main
import importlib

p1463 = importlib.import_module("1463")

class Testclass(TestCase):
    def test8958(self):
        testcase = [
            (1,0),
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
            (34,6),
            (35,7),
            (36,4),
            (37,5),
            (38,5),
            (39,5),
            (40,5),
            (41,6),
            (42,5),
            (42,5),
        ]
        self.numlist = [0] * 10**6
        for case, answer in testcase:
            self.assertEqual(p1463.sol(case, self.numlist), answer, f"{case}, {answer}")

if __name__=="__main__":
    main()