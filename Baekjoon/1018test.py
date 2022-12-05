from unittest import TestCase, main, mock
import importlib


p1018 = importlib.import_module('1018')


class testClass(TestCase):
    testcase = [
        (["8 8","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBBBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW"], 1),
        (["10 13","BBBBBBBBWBWBW","BBBBBBBBBWBWB","BBBBBBBBWBWBW","BBBBBBBBBWBWB","BBBBBBBBWBWBW","BBBBBBBBBWBWB","BBBBBBBBWBWBW","BBBBBBBBBWBWB","WWWWWWWWWWBWB","WWWWWWWWWWBWB"], 12),
    ]


    def test1193(self):
        for case, answer in testClass.testcase:
            with mock.patch('builtins.input', side_effect = case):
                self.assertEqual(p1018.solution(), answer, f'{case}, {answer}')


if __name__=='__main__':
    main()