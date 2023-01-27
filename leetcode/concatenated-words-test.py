from unittest import TestCase, main
import importlib
import unittest


problem = importlib.import_module('concatenated-words')


class testClass(TestCase):
    testcase = [
        ((['ab','aab','abaab', 'aabaabaab', 'abab', 'abb'],), {'abaab', 'aabaabaab', 'abab'}),
        ((['abab','bba','a', 'b', 'aab', 'ab'],), {'aab', 'ab', 'bba', 'abab'}),
    ]

    def testisConcatnate(self):
        solution = problem.Solution()
        solution.dictionary.add('ab')
        self.assertEqual(solution.isConcatenate('abab'), True)
        self.assertEqual(solution.isConcatenate('ab'), True)
        self.assertEqual(solution.isConcatenate('abb'), False)

    # @unittest.skip("잠시")
    def test1000(self):
        for case, answer in testClass.testcase:
            solution = problem.Solution()
            self.assertEqual(solution.findAllConcatenatedWordsInADict(*case), answer)
            print("=============================================================================")


if __name__=='__main__':
    main()