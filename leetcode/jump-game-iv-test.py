import importlib
from unittest import TestCase, main

problem = importlib.import_module("jump-game-iv")


class testClass(TestCase):
    testcase = [
        # (([100, -23, -23, 404, 100, 23, 23, 23, 3, 404],), 3),
        # (([7 for _ in range(5 * (10**4) - 1)] + [11],), 2),
        ((sum([[1, 2] for _ in range(24999)], []) + [7, 11],), 2),
    ]

    def test1000(self):
        solution = problem.Solution()
        for case, answer in testClass.testcase:
            self.assertEqual(solution.minJumps(*case), answer)


if __name__ == "__main__":
    main()
