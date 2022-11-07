from unittest import TestCase, mock, main
import importlib

p2231 = importlib.import_module("2231")

class CodeTest(TestCase):
    testcase = [
        ([216], 198),
        ([1234], 5),
        ([752], 5),
        ([4720], 5),
        ([10000], 5),
        ([75274], 5),
        ([785], 5),
        ([75], 5),
        ([45323], 5),
        ([193], 5),
        ([785], 5),
        ([32785], 5),
        ([994979], 5),
        ([9497], 5),
        ([9894], 5),
        ([992], 5),
        ([995], 5),
        ([994], 5),
        ([1000000], 5),
    ]

    def test2231(self):
        for k, answer in CodeTest.testcase:
            with mock.patch("builtins.input", side_effect=k):
                self.assertEqual(p2231.solution(), p2231.solution2(k[0]))

if __name__=="__main__":
    main()