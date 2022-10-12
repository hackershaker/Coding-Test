from unittest import TestCase, main
import importlib

p12978 = importlib.import_module("17683")
class Testclass(TestCase):
    def test12978(self):
        testcase = [("ABC", ["09:50,09:52,HELLO,C#DEFGAB", "09:50,09:51,WORLD,ABCDEF#"], "(None)"),
        ("ABC", ["09:50,09:55,HELLO,ABC#", "09:50,09:59,WORLD,CABCAB", "09:50,09:59,GEUST,CBACBA"], "WORLD"),
        ("AAA", ["09:50,09:55,HELLO,A#AA#AAA#AA", "09:50,09:52,WORLD,AAAA#", "09:50,09:54,GEUST,A#AAAAA#"], "GEUST"),
        ("AAA", ["09:50,09:50,HELLO,A#AA#AAA#AA", "09:50,09:54,WORLD,AAAA#", "09:50,09:54,GEUST,A#AAAAA#"], "WORLD"),
        ("AA#", ["09:50,09:53,HELLO,A#AA#AAA#AA", "09:50,09:54,WORLD,AAAA#", "09:50,09:54,GEUST,A#AAAAA#"], "WORLD"),
        ("A"*1439, ["00:00,23:59,HELLO,A", "09:50,09:54,WORLD,AAAA#", "09:50,09:54,GEUST,A#AAAAA#"], "HELLO"),
        ("EF#G#A#", ["00:00,23:59,HELLO,EF#G#AEF#", "09:50,09:56,WORLD,G#A#EF#", "09:50,09:54,GEUST,A#AAAAA#"], "WORLD"),
        ("EF#G#A#BC#", ["23:00,23:59,HELLO,A#BC#EF#G#A#BC#", "09:50,09:56,WORLD,G#A#BC#EF#", "09:50,09:54,GEUST,EF#G#A#BC#EF#G#A#BC#"], "HELLO"),
        ("CC#BCC#BCC#",  ["03:00,03:08,FOO,CC#B"], "FOO")
        ]

        for m, info, ans in testcase:
            self.assertEqual(p12978.solution(m, info), ans, f"failed testcase : {m, info}")


if __name__=="__main__":
    main()