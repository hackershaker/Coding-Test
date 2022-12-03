from unittest import TestCase, main, mock
import importlib


p1697 = importlib.import_module('1697')


class testClass(TestCase):
    testcase = [
        (['5 17'], 4),
        (['3 12'], 2),
        (['4 7'], 2),
        (['7 17'], 3),
    ]


    def test1193(self):
        for case, answer in testClass.testcase:
            with mock.patch('builtins.input', side_effect = case):
                self.assertEqual(p1697.solution(), answer, f"{case}, {answer}")


if __name__=='__main__':
    main()