from unittest import mock, TestCase, main
import importlib

p1149 = importlib.import_module("1149")

class testCode(TestCase):
    testcase = [
        [("3", "26 40 83", "49 60 57", "13 89 99"), 96],
        [("3", "1 100 100", "100 1 100", "100 100 1"), 3],
        [("3", "1 100 100", "100 100 100", "1 100 100"), 102],
        [("6", "30 19 5", "64 77 64", "15 19 97", "4 71 57", "90 86 84", "93 32 91"), 208],
        [("8", "71 39 44", "32 83 55", "51 37 63", "89 29 100", "83 58 11", "65 13 15", "47 25 29", "60 66 19"), 253],
        ]

    def test1149(self):
        for test_case, answer in testCode.testcase:
            with mock.patch("builtins.input", side_effect = test_case):
                self.assertEqual(p1149.solution(), answer, f"{test_case}, {answer}")

if __name__=="__main__":
    main()




    