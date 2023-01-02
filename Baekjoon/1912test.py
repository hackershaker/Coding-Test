from unittest import TestCase, main, mock
import importlib


p1912 = importlib.import_module('1912')


class testClass(TestCase):
    testcase = [
        (['10', '10 -4 3 1 5 6 -35 12 21 -1'], 33),
        (['10', '2 1 -4 3 4 -4 6 5 -5 1'], 14),
        (['5', '-1 -2 -3 -4 -5'], -1),
        (['5', '12 -4 2 -4 7'], 13),
        (['12', '1 5 -2 -4 6 8 -6 5 1 2 -4 -1'], 16),
        (['1', '-3'], -3),
    ]


    def test1912(self):
        for case, answer in testClass.testcase:
            with mock.patch('builtins.input', side_effect = case):
                self.assertEqual(p1912.solution(), answer, f'{case}, {answer}')


if __name__=='__main__':
    main()