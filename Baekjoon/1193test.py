from unittest import TestCase, main, mock
import importlib

p1193 = importlib.import_module("1193")

class testClass(TestCase):
    testcase = [
        (["1"], "1/1"),
        (["2"], "1/2"),
        (["3"], "2/1"),
        (["4"], "3/1"),
        (["5"], "2/2"),
        (["6"], "1/3"),
        (["7"], "1/4"),
        (["8"], "2/3"),
        (["9"], "3/2"),
        (["10"], "4/1"),
        (["11"], "5/1"),
        (["12"], "4/2"),
        (["13"], "3/3"),
        (["14"], "2/4"),
    ]

    def test1193(self):
        for i, answer in testClass.testcase:
            with mock.patch("builtins.input", side_effect = i):
                self.assertEqual(p1193.solution(), answer)

if __name__=="__main__":
    main()