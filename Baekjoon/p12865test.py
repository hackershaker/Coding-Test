from io import StringIO
import sys
from unittest import TestCase, main, mock
from p12865 import Solution


class testClass(TestCase):
    testcase = [
        (
            [
                "4 7",
                "6 13",
                "4 8",
                "3 6",
                "5 12",
            ],
            ["14"],
        ),
        (
            [
                "6 8",
                "2 3",
                "6 13",
                "4 8",
                "3 6",
                "5 12",
                "4 7",
            ],
            ["18"],
        ),
        (
            [
                "6 8",
                "2 3",
                "2 5",
                "2 3",
                "2 4",
                "4 12",
                "4 16",
            ],
            ["28"],
        ),
    ]

    def testProblem(self):
        for case, answer in testClass.testcase:
            with mock.patch("sys.stdin.readline", side_effect=case):
                capturedOutput = StringIO()
                sys.stdout = capturedOutput
                s = Solution()
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
