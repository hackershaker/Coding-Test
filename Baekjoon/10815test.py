from io import StringIO
import sys
from unittest import TestCase, main, mock
import importlib


p = importlib.import_module("10815")


class testClass(TestCase):
    testcase = [
        (
            ["5", "6 3 2 10 -10", "8", "10 9 -5 2 3 4 5 -10"],
            ["1 0 0 1 1 0 0 1"],
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
