from unittest import TestCase, main, mock
import importlib


p7576 = importlib.import_module('7576')


class testClass(TestCase):
    testcase = [
        (['6 4', '0 0 0 0 0 0','0 0 0 0 0 0','0 0 0 0 0 0','0 0 0 0 0 1'], 8),
        (['6 4', '0 -1 0 0 0 0','-1 0 0 0 0 0','0 0 0 0 0 0','0 0 0 0 0 1'], -1),
        (['6 4', '1 -1 0 0 0 0','0 -1 0 0 0 0','0 0 0 0 -1 0','0 0 0 0 -1 1'], 6),
        (['5 5', '-1 1 0 0 0','0 -1 -1 -1 0','0 -1 -1 -1 0','0 -1 -1 -1 0', '0 0 0 0 0'], 14),
        (['2 2', '1 -1','-1 1',], 0),
    ]


    def test1193(self):
        for case, answer in testClass.testcase:
            with mock.patch('builtins.input', side_effect = case):
                self.assertEqual(p7576.solution(), answer)


if __name__=='__main__':
    main()