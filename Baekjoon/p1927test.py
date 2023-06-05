from io import StringIO
import sys
from unittest import TestCase, main, mock
from p1927 import Solution


class testClass(TestCase):
    testcase = [
        (
            ["11", "0", "5", "1", "4", "2", "3", "0", "0", "0", "0", "0"],
            ["0", "1", "2", "3", "4", "5"],
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
