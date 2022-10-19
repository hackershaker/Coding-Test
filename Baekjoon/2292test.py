from unittest import TestCase, main
import importlib

p2292 = importlib.import_module("2292")
class testClass(TestCase):
    testcase = [
        (4,2),
        (19,3),
        (31,4),
        (13,3),
        (25,4),
        (38,5),
        (59,5),
        (60,5),
    ]
    def test2292(self):
        for case, ans in testClass.testcase:
            self.assertEqual(p2292.solution(case), ans, f"{case},{ans}")

    def testgetfloor(self):
        self.assertEqual(p2292.getfloor(7), 2)
        self.assertEqual(p2292.getfloor(1), 1)
        self.assertEqual(p2292.getfloor(20), 4)
        self.assertEqual(p2292.getfloor(66), 6)

if __name__=="__main__":
    main()

















































































