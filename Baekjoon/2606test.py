from unittest import TestCase, main, mock
import importlib

p2606 = importlib.import_module("2606")

class testClass(TestCase):
    testcase = [
        (["7","6","1 2","2 3","1 5","5 2","5 6","4 7"], 4),
    ]

    def test2606(self):
        for inputset, answer in testClass.testcase:
            with mock.patch("builtins.input", side_effect = inputset):
                self.assertEqual(p2606.solution(), answer)

if __name__=="__main__":
    main()