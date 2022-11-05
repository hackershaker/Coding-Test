from unittest import mock, TestCase, main
import importlib

p2178 = importlib.import_module("2178")

class testClass(TestCase):
    testcase = [
        (["4 6", "101111", "101010", "101011", "111011"], 15),
        (["4 6", "110110", "110110", "111111", "111101"], 9),
        (["2 25", "1011101110111011101110111", "1110111011101110111011101"], 38),
        (["7 7", "1011111", "1110001", "1000001", "1000001", "1000001", "1000001", "1111111"], 13),
    ]

    def test2178(self):
        for case, answer in testClass.testcase:
            with mock.patch("builtins.input", side_effect=case):
                self.assertEqual(p2178.solution(), answer, f"{case}, {answer}")

if __name__=="__main__":
    main()