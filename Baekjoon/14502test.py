from io import StringIO
import sys
from unittest import TestCase, main, mock
import importlib


p = importlib.import_module("14502")


class testClass(TestCase):
    testcase = [
        (
            [
                "3 3",
                "2 2 0",
                "0 0 0",
                "0 0 0",
            ],
            ["4"],
        ),
        (
            [
                "7 7",
                "2 0 0 0 1 1 0",
                "0 0 1 0 1 2 0",
                "0 1 1 0 1 0 0",
                "0 1 0 0 0 0 0",
                "0 0 0 0 0 1 1",
                "0 1 0 0 0 0 0",
                "0 1 0 0 0 0 0",
            ],
            ["27"],
        ),
        (
            [
                "4 6",
                "0 0 0 0 0 0",
                "1 0 0 0 0 2",
                "1 1 1 0 0 2",
                "0 0 0 0 0 2",
            ],
            ["9"],
        ),
        (
            [
                "8 8",
                "2 0 0 0 0 0 0 2",
                "2 0 0 0 0 0 0 2",
                "2 0 0 0 0 0 0 2",
                "2 0 0 0 0 0 0 2",
                "2 0 0 0 0 0 0 2",
                "0 0 0 0 0 0 0 0",
                "0 0 0 0 0 0 0 0",
                "0 0 0 0 0 0 0 0",
            ],
            ["3"],
        ),
    ]

    def testProblem(self):
        for case, answer in testClass.testcase:
            with mock.patch("sys.stdin.readline", side_effect=case):
                capturedOutput = StringIO()
                sys.stdout = capturedOutput
                s = p.Solution()
                s.solution()
                sys.stdout = sys.__stdout__
                result = capturedOutput.getvalue()
                self.assertEqual(
                    result, testClass.makeLine(answer), f"{case}, {answer}"
                )
                print(capturedOutput.getvalue())

    @staticmethod
    def makeLine(arr) -> str:
        answer = ""
        for s in arr:
            answer += str(s) + "\n"
        return answer


if __name__ == "__main__":
    main()
