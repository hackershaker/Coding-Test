from unittest import TestCase, main
import importlib

p72411 = importlib.import_module("72411")
class TestClass(TestCase):
    def testcode(self):
        testcase = [(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4], ["AC", "ACDE", "BCFG", "CDE"]),
        (["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5], ["ACD", "AD", "ADE", "CD", "XYZ"]),
        (["XYZ", "XWY", "WXA"], [2, 3, 4], ["WX", "XY"]),
        ]

        for o, c, ans in testcase:
            self.assertEqual(p72411.solution(o, c), ans, f"testcase is {o}, {c}")

if __name__=="__main__":
    main()