from io import StringIO
import sys
from unittest import TestCase, main, mock
import importlib


p14501 = importlib.import_module("14501")


class testClass(TestCase):
    testcase = [
        (["7", "3 10", "5 20", "1 10", "1 20", "2 15", "4 40", "2 200"], ["45"]),
        (
            [
                "10",
                "1 1",
                "1 2",
                "1 3",
                "1 4",
                "1 5",
                "1 6",
                "1 7",
                "1 8",
                "1 9",
                "1 10",
            ],
            ["55"],
        ),
        (
            [
                "10",
                "5 50",
                "4 40",
                "3 30",
                "2 20",
                "1 10",
                "1 10",
                "2 20",
                "3 30",
                "4 40",
                "5 50",
            ],
            ["90"],
        ),
    ]

    def test14501(self):
        for case, answer in testClass.testcase:
            with mock.patch("sys.stdin.readline", side_effect=case):
                capturedOutput = StringIO()
                sys.stdout = capturedOutput
                s = p14501.Solution()
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
