from unittest import TestCase, main, mock
import importlib


p14715 = importlib.import_module('14715')


class testClass(TestCase):
    testcase = [
        (['24'], 2),
        (['3'], 0),
        (['4'], 1),
        (['6'], 1),
        (['8'], 2),
        (['9'], 1),
        (['16'], 2),
        (['18'], 2),
        (['20'], 2),
        (['27'], 2),
        (['28'], 2),
        (['23'], 0),
        (['10'], 1),
        (['15'], 1),
        (['60'], 2),
        (['72'], 3),
        ([str(6**4)], 3),
    ]


    def test14715(self):
        for case, answer in testClass.testcase:
            with mock.patch('builtins.input', side_effect = case):
                self.assertEqual(p14715.solution(), answer, f'{case}, {answer}')


if __name__=='__main__':
    main()