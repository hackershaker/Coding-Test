from unittest import TestCase, main, mock
import importlib

p7568 = importlib.import_module("7568")

class testClass(TestCase):
    testcase = [
        (["5","55 185","58 183","88 186","60 175","46 155"], [2, 2, 1, 2, 5]),
        (["5","55 185","55 183","88 186","50 165","46 155"], [2, 2, 1, 4, 5]),
        (["2","80 185","55 170"], [1, 2,]),
        (["2","80 185","85 170"], [1, 1,]),
        (["3","80 185","80 170", "80 173"], [1, 1, 1]),
        (["4","80 185", "80 170" ,"75 170", "60 185"], [1, 1, 2, 1]),
    ]

    def test7568(self):
        for inputset, answer in testClass.testcase:
            with mock.patch("builtins.input", side_effect = inputset):
                self.assertEqual(p7568.solution(), answer)

if __name__=="__main__":
    main()