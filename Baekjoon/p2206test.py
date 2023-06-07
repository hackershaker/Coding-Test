from io import StringIO
import sys
from unittest import TestCase, main, mock
from p2206 import Solution


class testClass(TestCase):
    testcase = [
        (
            [
                "6 4",
                "0100",
                "1110",
                "1000",
                "0000",
                "0111",
                "0000",
            ],
            ["15"],
        ),
        (
            [
                "4 4",
                "0111",
                "1111",
                "1111",
                "1110",
            ],
            ["-1"],
        ),
        (
            [
                "8 9",
                "011110000",
                "011110110",
                "000000110",
                "011111110",
                "011111110",
                "011111110",
                "011111110",
                "100000000",
            ],
            ["16"],
        ),
        (
            [
                "10 9",
                "011110000",
                "011110110",
                "000000110",
                "011111110",
                "000010000",
                "011111110",
                "011111110",
                "011110000",
                "011110110",
                "000000110",
            ],
            ["18"],
        ),
        (
            [
                "100 100",
            ]
            + ["0" * 100 for _ in range(100)],
            ["199"],
        ),
        (
            [
                "1000 1000",
            ]
            + ["0" * 1000 for _ in range(1000)],
            ["1999"],
        ),
        (
            [
                "1 1",
                "0",
            ],
            ["1"],
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
