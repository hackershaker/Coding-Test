from unittest import TestCase, main
import importlib

p12971 = importlib.import_module("12971")
class Testclass(TestCase):
    def testmakeDelSet(self):
        testcase = [
            ([14, 6, 5, 11, 3, 9, 2, 10], 36),
            ([14, 6, 9, 11, 10, 5, 11, 10], 44),
            ([1, 3, 2, 5, 4], 8),
            ([20, 3, 2, 5, 4], 20+5),
            ([4,3,2,1,2,3,4], 9),
            ([4,3,2,1,3,2,4], 10),
            ([10, 8, 5, 7, 2, 1, 2, 3], 10+7+2),
            ([2,2,3,4,3,2,2], 3+3+2),
            ([5,2,3,4,5,2,4], 5+3+5),
            ([9,7,2,3,4,5,2,6], 7+6+3+5),
            ([4], 4),
            ([2,3], 3),
            ([3,4,5], 5),
            ([2,4,2], 4),
        ]

        for sticker, ans in testcase:
            print(sticker, ans)
            self.assertEqual(p12971.solution(sticker), ans, f"failed testcase : {sticker, ans}")


if __name__=="__main__":
    main()