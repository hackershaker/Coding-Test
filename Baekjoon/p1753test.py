from io import StringIO
import sys
from unittest import TestCase, main, mock
from p1753 import Solution


class testClass(TestCase):
    testcase = [
        (
            [
                "5 6",
                "1",
                "5 1 1",
                "1 2 2",
                "1 3 3",
                "2 3 4",
                "2 4 5",
                "3 4 6",
            ],
            [
                "0",
                "2",
                "3",
                "7",
                "INF",
            ],
        ),
        (
            [
                "3 3",
                "1",
                "1 2 1",
                "2 3 2",
                "3 1 3",
            ],
            [
                "0",
                "1",
                "3",
            ],
        ),
        (
            [
                "4 4",
                "1",
                "1 2 1",
                "2 3 2",
                "3 4 3",
                "4 2 1",
            ],
            [
                "0",
                "1",
                "3",
                "6",
            ],
        ),
        (
            [
                "5 6",
                "1",
                "1 2 10",
                "1 2 8",
                "1 4 1",
                "2 3 2",
                "3 4 3",
                "4 2 1",
            ],
            [
                "0",
                "2",
                "4",
                "1",
                "INF",
            ],
        ),
        (
            [
                "3 6",
                "1",
                "3 2 10",
                "3 2 8",
                "2 3 3",
                "2 3 2",
                "3 2 3",
                "2 3 3",
            ],
            [
                "0",
                "INF",
                "INF",
            ],
        ),
        (
            [
                "3 6",
                "1",
                "3 1 10",
                "3 1 8",
                "2 1 3",
                "2 1 2",
                "3 1 3",
                "2 1 3",
            ],
            [
                "0",
                "INF",
                "INF",
            ],
        ),
        (
            [
                "4 3",
                "1",
                "1 2 10",
                "2 3 10",
                "3 4 10",
            ],
            [
                "0",
                "10",
                "20",
                "30",
            ],
        ),
        (
            [
                "6 11",
                "1",
                "1 2 1",
                "1 3 10",
                "1 6 6",
                "1 6 2",
                "2 3 1",
                "3 4 1",
                "3 5 4",
                "3 6 5",
                "4 1 7",
                "4 5 1",
                "5 6 1",
            ],
            [
                "0",
                "1",
                "2",
                "3",
                "4",
                "2",
            ],
        ),
        (
            [
                "7 3",
                "1",
                "1 2 6",
                "1 3 3",
                "3 2 1",
            ],
            [
                "0",
                "4",
                "3",
                "INF",
                "INF",
                "INF",
                "INF",
            ],
        ),
        (  # 위상정렬을 활용할 때 오류가 남. 노드3을 출발점으로 계산하면 노드 2가 갱신되어서 2에서 한 번 더 갱신을 해야 하는데 이미 visited에 있어서 갱신이 안 됨.
            [
                "7 22",
                "1",
                "1 2 6",
                "1 3 3",
                "1 4 4",
                "1 5 6",
                "1 6 5",
                "1 7 8",
                "2 3 10",
                "2 4 2",
                "2 5 5",
                "2 6 1",
                "2 7 4",
                "3 2 1",
                "3 4 9",
                "3 5 7",
                "3 6 7",
                "3 7 4",
                "4 5 2",
                "4 6 7",
                "4 7 1",
                "5 6 1",
                "5 7 3",
                "6 7 2",
            ],
            [
                "0",
                "4",
                "3",
                "4",
                "6",
                "5",
                "5",
            ],
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
