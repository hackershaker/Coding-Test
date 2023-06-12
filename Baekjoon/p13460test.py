from io import StringIO
import sys
from unittest import TestCase, main, mock
from p13460 import Solution


class testClass(TestCase):
    testcase = [
        (
            [
                "5 5",
                "#####",
                "#..B#",
                "#.#.#",
                "#RO.#",
                "#####",
            ],
            ["1"],
        ),
        (
            [
                "7 7",
                "#######",
                "#...RB#",
                "#.#####",
                "#.....#",
                "#####.#",
                "#O....#",
                "#######",
            ],
            ["5"],
        ),
        (
            [
                "7 7",
                "#######",
                "#..R#B#",
                "#.#####",
                "#.....#",
                "#####.#",
                "#O....#",
                "#######",
            ],
            ["5"],
        ),
        (
            [
                "10 10",
                "##########",
                "#R#...##B#",
                "#...#.##.#",
                "#####.##.#",
                "#......#.#",
                "#.######.#",
                "#.#....#.#",
                "#.#.#.#..#",
                "#...#.O#.#",
                "##########",
            ],
            ["-1"],
        ),
        (
            [
                "3 7",
                "#######",
                "#R.O.B#",
                "#######",
            ],
            ["1"],
        ),
        (
            [
                "10 10",
                "##########",
                "#R#...##B#",
                "#...#.##.#",
                "#####.##.#",
                "#......#.#",
                "#.######.#",
                "#.#....#.#",
                "#.#.##...#",
                "#O..#....#",
                "##########",
            ],
            ["7"],
        ),
        (
            [
                "3 10",
                "##########",
                "#.O....RB#",
                "##########",
            ],
            ["-1"],
        ),
        (
            [
                "7 7",
                "#######",
                "#R###.#",
                "#B..###",
                "#.##..#",
                "#.###.#",
                "#O....#",
                "#######",
            ],
            ["2"],
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
