from io import StringIO
import sys
from unittest import TestCase, main, mock
from p10026 import Solution


class testClass(TestCase):
    testcase = [
        (
            [
                "2",
                "RG",
                "BR",
            ],
            ["4 2"],
        ),
        (
            [
                "5",
                "RRRBB",
                "GGBBB",
                "BBBRR",
                "BBRRR",
                "RRRRR",
            ],
            ["4 3"],
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
