from unittest import TestCase, main
import importlib

p11047 = importlib.import_module("11047")

class Testclass(TestCase):
    def test8958(self):
        testcase = [
            ([1,5,10,50,100,500,1000,5000,10000,50000], 4200, 6),
            ([1,5,10,50,100,500,1000,5000,10000,50000], 4790, 12),
            ([1,5,10,50,100,500,1000,5000,10000,50000], 1210, 4),
        ]

        for value, k, answer in testcase:
            self.assertEqual(p11047.solution(value, k), answer)

if __name__=="__main__":
    main()