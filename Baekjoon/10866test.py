from io import StringIO
import sys
from unittest import TestCase, main, mock
import importlib


p10866 = importlib.import_module('10866')


class testClass(TestCase):
    testcase = [
        ( ['15','push_back 1','push_front 2','front','back','size','empty','pop_front','pop_back','pop_front','size','empty','pop_back','push_front 3','empty','front',], ['2','1','2','0','2','1','-1','0','1','-1','0','3',] ),
        ( ['22','front','back','pop_front','pop_back','push_front 1','front','pop_back','push_back 2','back','pop_front','push_front 10','push_front 333','front','back','pop_back','pop_back', 'push_back 20', 'push_back 1234', 'front', 'back', 'pop_back', 'pop_back'], ['-1','-1','-1','-1','1','1','2','2','333','10','10','333','20','1234','1234','20'] ), 
        ( ['6','pop_back','pop_front', 'empty', 'size', 'front', 'back'], ['-1','-1', '1', '0', '-1', '-1'] ),
        ( ['12','push_back 1','push_front 2', 'push_front 3', 'push_back 4', 'front', 'back', 'pop_front', 'pop_front', 'pop_front', 'empty', 'pop_front', 'pop_front'], ['3','4','3','2','1','0', '4','-1'] ),
        ( ['9','push_front 5','push_front 6', 'push_back 9', 'push_back 2', 'back', 'push_front 4', 'back', 'pop_back', 'back',], ['2','2','2','9'] ),
        ( ['1','push_front 5',], [] ),
    ]

    def test10866(self):
        for case, answer in testClass.testcase:
            with mock.patch('sys.stdin.readline', side_effect = case):
                capturedOutput = StringIO()
                sys.stdout = capturedOutput
                p10866.solution()
                sys.stdout = sys.__stdout__
                result = capturedOutput.getvalue()
                self.assertEqual(result, testClass.makeLine(answer))
                print(result)

    @staticmethod
    def makeLine(arr) -> str:
        answer = ''
        for s in arr:
            answer += str(s) + "\n"
        return answer

if __name__=='__main__':
    main()