from unittest import TestCase, main, mock
import importlib


p1012 = importlib.import_module('1012')


class testClass(TestCase):
    testcase = [
        (['1', '5 5 3', '1 0', '1 1', '3 3'], [2,1]),
    ]


    def test1012(self):
        for case, answer in testClass.testcase:
            with mock.patch('builtins.input', side_effect = case):
                self.assertEqual(p1012.solution(), answer)


if __name__=='__main__':
    main()