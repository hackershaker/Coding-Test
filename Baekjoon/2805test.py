from io import StringIO
import sys
from unittest import TestCase, main, mock, skip
import importlib


p2805 = importlib.import_module('2805')


class testClass(TestCase):
    testcase = [
        ( ['4 7', '20 15 10 17'], ['15'] ),
        ( ['5 20', '4 42 40 26 46'], ['36'] ),
        ( ['1 15', '20'], ['5'] ),
        ( ['2 17', '8 16'], ['3'] ),
        ( ['5 1', '3 4 5 2 8'], ['7'] ),
        ( ['5 2', '3 4 5 2 8'], ['6'] ),
        ( ['5 3', '3 4 5 2 8'], ['5'] ),
        ( ['5 4', '3 4 5 2 8'], ['4'] ),
        ( ['5 5', '3 4 5 2 8'], ['4'] ),
    ]

    def testPrint(self):
        for case, answer in testClass.testcase:
            with mock.patch('sys.stdin.readline', side_effect = case):
                solution = p2805.Solution()
                result = solution.getMaximumHeight()
                self.assertEqual(result, int(answer[0]), f"{case}, {answer}")
                print("==========================================================")

    # @skip("")
    def test2805(self):
        for case, answer in testClass.testcase:
            with mock.patch('sys.stdin.readline', side_effect = case):
                capturedOutput = StringIO()
                sys.stdout = capturedOutput
                solution = p2805.Solution()
                solution.getMaximumHeight()
                sys.stdout = sys.__stdout__
                result = capturedOutput.getvalue()
                self.assertEqual(result, testClass.makeLine(answer), f"{case}, {answer}")
                print(capturedOutput.getvalue())


    @staticmethod
    def makeLine(arr) -> str:
        answer = ''
        for s in arr:
            answer += str(s) + '\n'
        return answer


if __name__=='__main__':
    main()