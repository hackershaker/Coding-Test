from unittest import TestCase, main, mock
import importlib


p1931 = importlib.import_module('1931')


class testClass(TestCase):
    testcase = [
        (['4', '1 2', '4 7', '5 6', '6 8'], 3),
        (['4', '1 2', '2 4', '5 6', '6 8'], 4),
    ]


    def test1193(self):
        for case, answer in testClass.testcase:
            with mock.patch('builtins.input', side_effect = case):
                self.assertEqual(p1931.solution(), answer)


if __name__=='__main__':
    main()