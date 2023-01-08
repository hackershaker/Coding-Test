from unittest import TestCase, main, mock
import importlib


p2156 = importlib.import_module('2156')


class testClass(TestCase):
    testcase = [
        (['6','6','10','13','9','8','1'], 33),
        (['3','2','10','9'], 19),
        (['2','4','10'], 14),
        (['1','10'], 10),
    ]


    def test2156(self):
        for case, answer in testClass.testcase:
            with mock.patch('builtins.input', side_effect = case):
                self.assertEqual(p2156.solution(), answer, f'{case}, {answer}')


if __name__=='__main__':
    main()