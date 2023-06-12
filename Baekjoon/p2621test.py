from io import StringIO
import sys
from unittest import TestCase, main, mock
from p2621 import Solution


class testClass(TestCase):
    testcase = [
        (
            [
                "Y 4",
                "Y 3",
                "Y 2",
                "Y 5",
                "Y 6",
            ],
            ["906"],
        ),
        (["B 3", "R 3", "B 7", "Y 3", "G 3"], ["803"]),
        (["R 5", "Y 5", "G 7", "B 5", "Y 7"], ["757"]),
        (["Y 3", "Y 4", "Y 8", "Y 6", "Y 7"], ["608"]),
        (["R 7", "R 8", "G 9", "Y 6", "B 5"], ["509"]),
        (["R 7", "Y 7", "R 2", "G 7", "R 5"], ["407"]),
        (["R 5", "Y 5", "Y 4", "G 9", "B 4"], ["354"]),
        (["R 5", "Y 2", "B 5", "B 3", "G 4"], ["205"]),
        (["R 1", "R 2", "B 4", "B 8", "Y 5"], ["108"]),
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
