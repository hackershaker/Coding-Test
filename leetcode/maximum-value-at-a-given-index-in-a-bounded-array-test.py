from unittest import TestCase, main, skip
import importlib


problem = importlib.import_module("maximum-value-at-a-given-index-in-a-bounded-array")


class testClass(TestCase):
    testcase = [
        (("test",), "answer"),
    ]

    def testsumArray(self):
        s = problem.Solution()
        self.assertEqual(s.sumArray(4, 2, 1), 4)
        self.assertEqual(s.sumArray(4, 2, 2), 5)
        self.assertEqual(s.sumArray(4, 3, 3), 7)

    @skip("")
    def test1000(self):
        solution = problem.Solution()
        for case, answer in testClass.testcase:
            self.assertEqual(solution.methodNameInsertHere(*case), answer)


if __name__ == "__main__":
    main()
