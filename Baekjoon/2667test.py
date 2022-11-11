from unittest import TestCase, main, mock
import importlib

p2667 = importlib.import_module("2667")

class testClass(TestCase):
    testcase = [
        (["7","0110100","0110101","1110101","0000111","0100000","0111110","0111000"], [7,8,9]),
    ]

    def test2667(self):
        for inputset, answer in testClass.testcase:
            with mock.patch("builtins.input", side_effect = inputset):
                self.assertEqual(p2667.solution(), answer)

if __name__=="__main__":
    main()