from unittest import TestCase, main
import importlib


p67259 = importlib.import_module('67259')


class testClass(TestCase):
    testcase = [
        (([[0, 0, 0], [0, 0, 0], [0, 0, 0]],), 900),
        (([[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]],), 3800),
        (([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]],), 2100),
        (([[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]],), 3200),
    ]


    def test67259(self):
        for case, answer in testClass.testcase:
            self.assertEqual(p67259.solution(*case), answer)


if __name__=='__main__':
    main()