from io import StringIO
import sys
from unittest import TestCase, main, mock
import importlib


p11724 = importlib.import_module('11724')


class testClass(TestCase):
    testcase = [
        ( ['6 5','1 2','2 5','5 1','3 4','4 6',], ['2'] ),
        ( ['6 8','1 2','2 5','5 1','3 4','4 6','5 4','2 4','2 3',], ['1'] ),
        ( ['6 0'], ['6'] ),
    ]


    def test11724(self):
        for case, answer in testClass.testcase:
            with mock.patch('sys.stdin.readline', side_effect = case):
                capturedOutput = StringIO()
                sys.stdout = capturedOutput
                p11724.solution()
                sys.stdout = sys.__stdout__
                result = capturedOutput.getvalue()
                self.assertEqual(result, testClass.makeLine(answer))
                print(capturedOutput.getvalue())


    @staticmethod
    def makeLine(arr) -> str:
        answer = ''
        for s in arr:
            answer += str(s) + '\n'
        return answer


if __name__=='__main__':
    main()