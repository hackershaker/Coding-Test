def solution():
    numlist = []
    for _ in range(int(input())):
        if (x := input()) not in numlist:
            numlist.append(x)
    
    numlist.sort(key=lambda x: (len(x), x))
    for num in numlist:
        print(num)
    return numlist

if __name__=="__main__":
    solution()

from unittest import TestCase, mock, main
class codeTest(TestCase):
    testcase = [
        [(13,"but","i","wont","hesitate","no","more","no","more","it","cannot","wait","im","yours"), ['i','im','it','no','but','more','wait','wont','yours','cannot','hesitate']],
        [(5,"is","it","isp","iat","ibb"), ['is','it','iat','ibb','isp']],
        [(5,"is","is","isp","iat","ibb"), ['is','iat','ibb','isp']],
        [(1,"is"), ['is']],
    ]
    def test1181(self):
        for case, answer in codeTest.testcase:
            with mock.patch("builtins.input", side_effect=case):
                self.assertEqual(solution(), answer)
                print("==========================================================")
            
