from unittest import TestCase, main
import importlib

p42860 = importlib.import_module("42860")
class TestClass(TestCase):
    def testchange(self):
        testcase = [
            ("A","B", 1),
            ("C","Z", 3),
            ("Z","X", 2),
            ("W","C", 6),
            ("A","G", 6),
            ("A","A", 0),
            ("A","C", 2),

        ]

        for before, after, answer in testcase:
            self.assertEqual(p42860.change(before, after), answer, f"testcase is {before}, {after}, {answer}")
    

    def testmoveleft(self):
        testcase = [
            ("AAAAAAAAAAAAAAA", 4 ,"DYAOAAAARQANAWA", (3,1)),
            ("AAAAAAAAAA", 2 ,"DYAOAAAARQ", (1,1)),
            ("AAAAAAAAAA", 2 ,"AAAOAAAARQ", (9,3)),
            ("AAA", 1 ,"ABC", (2,2)),
            ("ABA", 1 ,"ABC", (2,2)),
            ("AAC", 2 ,"ABC", (1,1)),
        ]

        for wordlist, idx, name, ans in testcase:
            self.assertEqual(p42860.findleft(wordlist, idx, name), ans, f"testcase is {wordlist}, {idx}, {name}")
    
    def testmoveright(self):
        testcase = [
            ("AAAAAAAAAAAAAAA", 4 ,"DYAOAAAARQANAWA", (8,4)),
            ("AAAAAAAAAA", 2 ,"DYAOAAAARQ", (3,1)),
            ("AAAAAAAAAA", 2 ,"AQAAAAAAAA", (1,9)),
            ("AAAAAAAAAA", 7 ,"AQAAAAAAAA", (1,4)),
            ("AAC", 2 ,"ABC", (1,2)),
        ]

        for wordlist, idx, name, ans in testcase:
            self.assertEqual(p42860.findright(wordlist, idx, name), ans, f"testcase is {wordlist}, {idx}, {name}")

    def testsolution(self):
        testcase = [
            ("ABC", 5),
            ("ZZA", 3),
            ("CBABC", 10),
            ("DOG", 23),
            ("JAN", 23),
            ("AAADFX", 14),
            ("AGDEA", 16),
            ("JEROEN", 56),
            ("JAZ", 11),
            ("CAZAA", 5),
            ("CZAB", 7),
            ("AAAA", 0),
            ("BAAB", 3),
            ("ABAABCA", 2+4+3),
            ("ABADABCAG", 21),
            ("ABCAG", 2+3+8),
            ("EDCBAE", 4+4+3+2+6),
            ("AAEEAA", 6+5),
            ("AAEEA", 6+5),
            ("CBACBA", 2+2+4+2),
            ("ABZYABCAZAZ", 2+2+3+3+3+3+3),
            ("ABAAB", 5),
            ("AAIAPB", 24),
            ("DYAOAAAARQANAWA", 66),
            ("ASWAAATDAJAXA", 45),
            ("BADADC", 1+3+4+5),
            ("BADDAC", 1+3+4+5),
            ("BADADAC", 1+3+5+5), # B C D D
            ("ABADADAC", 2+4+5+5),
            ("AAABBAAAABBAAAAAAA", 4+2+6+2),
            ("AABBBAAAABBAAAABA", 3+5+2+2+6+2),
            ("ABABAAAAAAABA", 10),
            ("AZAAAAAAZAZA", 2+4+3),
            ("AZAAZAAAZAZA", 2+4+3+5),
        ]

        for word, answer in testcase:
            self.assertEqual(p42860.solution(word), answer, f"testcase is {word}, {answer}") 

if __name__=="__main__":
    main()