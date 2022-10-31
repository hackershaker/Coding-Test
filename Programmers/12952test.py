from unittest import TestCase, main
import importlib

p12952 = importlib.import_module("12952")
class Testclass(TestCase):
    def testmakeDelSet(self):
        testcase = [
            ([(0,1)], 3, {(0,0), (0,2), (1,1), (2,1), (1,0), (1,2)}),
        ]

        for path, n, ans in testcase:
            self.assertEqual(p12952.makeDelSet(path, n), ans, f"failed testcase : {path, n, ans}")


if __name__=="__main__":
    main()