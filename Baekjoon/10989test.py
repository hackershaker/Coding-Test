from unittest import TestCase, main, mock
import importlib

p10989 = importlib.import_module("10989")

class testClass(TestCase):
    testcase = [
        (["7","4","2","3","6","4","7","2"], [2,2,3,4,4,6,7]),
        (["10","5","2","3","1","4","2","3","5","1","7"], [1,1,2,2,3,3,4,5,5,7]),
    ]

    def test10989(self):
        for inputset, answer in testClass.testcase:
            with mock.patch("sys.stdin.readline", side_effect = inputset):
                self.assertEqual(p10989.solution(), answer)

if __name__=="__main__":
    main()