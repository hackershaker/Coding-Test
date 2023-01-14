from unittest import TestCase, main
import importlib


problem = importlib.import_module('lexicographically-smallest-equivalent-string')


class testClass(TestCase):
    testcase = [
        (("parker","morris","parser"), "makkek"),
        (("hello","world","hold"), "hdld"),
        (("leetcode","programs","sourcecode"), "aauaaaaada"),
        (("dfeffdfafbbebbebacbbdfcfdbcacdcbeeffdfebbdebbdafff","adcdfabadbeeafeabbadcefcaabdecabfecffbabbfcdfcaaae","myickvflcpfyqievitqtwvfpsrxigauvlqdtqhpfugguwfcpqv"), "myiakvalapayqiavitqtwvapsrxigauvlqatqhpaugguwaapqv"),
    ]


    def test1000(self):
        solution = problem.Solution()
        for case, answer in testClass.testcase:
            self.assertEqual(solution.smallestEquivalentString(*case), answer)
            print("============================================")


if __name__=='__main__':
    main()