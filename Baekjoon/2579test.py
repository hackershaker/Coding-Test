from unittest import TestCase, main, mock
import importlib


p2579 = importlib.import_module('2579')


class testClass(TestCase):
    testcase = [
        (['6', '10', '20', '15', '25', '10', '20'], 75),
        (['300'] + ['10'] * 300, 750),
    ]


    def test1193(self):
        for case, answer in testClass.testcase:
            with mock.patch('builtins.input', side_effect = case):
                self.assertEqual(p2579.solution(), answer)


if __name__=='__main__':
    main()