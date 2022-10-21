from unittest import TestCase, main
import importlib

p2941 = importlib.import_module("2941")

class testClass(TestCase):
    testcase = [
        ("ljes=njak", 6),
        ("ddz=z=", 3),
        ("nljj", 3),
        ("c=c=", 2),
        ("dz=ak", 3),
        ("s=z=dz=c=dd-", 6),
        ("dcz=", 3),
    ]
        
    

    def test2941(self):
        for case, answer in testClass.testcase:
            self.assertEqual(p2941.solution(case), answer, f"{case}, {answer}")

if __name__=="__main__":
    main()