from pprint import pprint
from unittest import TestCase, main
import importlib
import unittest


problem = importlib.import_module('snakes-and-ladders')


class testClass(TestCase):
    testcase = [
        (([[-1,-1],[-1,3]],), 1),
        (([[-1,-1,-1,],[2,2,2,],[-1,4,4,],],), 2),
        (([[1,1,-1],[1,1,1],[-1,1,1]],), -1),
        (([[-1,-1,-1,-1,],[-1,-1,-1,-1,],[2,2,-1,-1,],[-1,6,6,-1,],],), 3),
        (([[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]],), 4),
        (([[-1,-1,-1,-1,48,5,-1],[12,29,13,9,-1,2,32],[-1,-1,21,7,-1,12,49],[42,37,21,40,-1,22,12],[42,-1,2,-1,-1,-1,6],[39,-1,35,-1,-1,39,-1],[-1,36,-1,-1,-1,-1,5]],), 3),
    ]

    def testconvertOrd(self):
        self.assertEqual(problem.Solution.convertOrd(1,6), (5,0))
        self.assertEqual(problem.Solution.convertOrd(4,6), (5,3))
        self.assertEqual(problem.Solution.convertOrd(8,6), (4,4))
        self.assertEqual(problem.Solution.convertOrd(13,6), (3,0))
        self.assertEqual(problem.Solution.convertOrd(14,6), (3,1))
        self.assertEqual(problem.Solution.convertOrd(20,5), (1,0))
        self.assertEqual(problem.Solution.convertOrd(4,2), (0,0))

    # @unittest.skip("skip for previous tests")
    def test1000(self):
        solution = problem.Solution()
        for case, answer in testClass.testcase:
            pprint(case)
            self.assertEqual(solution.snakesAndLadders(*case), answer, print(f"testcase: {case}, answer: {answer}"))
            print("======================================================End of TestCase======================================================")


if __name__=='__main__':
    main()