from unittest import TestCase, mock, main
import io, sys

from p1002 import solution

class BaekjoonTest(TestCase):
    def test1002(self):
        testcase = [
            "0 0 13 40 0 37",
            "0 0 3 0 7 4",
            "1 1 1 1 1 5",
        ]
        answer = ["2", "1", "0"]
        mock_input.return_value = yield testcase
        for m, a in zip(mock_input, answer):
            capturedoutput = io.StringIO
            sys.stdout = capturedoutput
            solution(m)
            print(capturedoutput)
            self.assertEqual(capturedoutput, a)
        return

if __name__=="__main__":
    main()