from unittest import TestCase, main

from p1002 import solution

class BaekjoonTest(TestCase):
    def test1002(self):
        testcase = [
            "0 0 13 40 0 37",
            "0 0 3 0 7 4",
            "1 1 1 1 1 5",
            "1 1 2 1 1 2", #겹치는 원
            "1 0 2 2 0 3", #내접
            "1 0 2 6 0 2",
            "0 0 1 3 4 4",
            "0 0 1 3 0 9",
        ]
        answer = ["2", "1", "0", "-1", "1", "0", "1", "0"]
        for case, ans in zip(testcase, answer):
            self.assertEqual(solution(case), int(ans), f"testcase: {case}")
        return

if __name__=="__main__":
    main()