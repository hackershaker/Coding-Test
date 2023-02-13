from collections import Counter
import sys


class Solution:
    @classmethod
    def solution(cls):
        n = int(sys.stdin.readline().rstrip())
        card = Counter(sys.stdin.readline().rstrip().split(" "))

        m = int(sys.stdin.readline().rstrip())
        answer = ""
        for num in sys.stdin.readline().rstrip().split(" "):
            answer += " " + str(card[num])

        answer = answer.lstrip()
        print(answer)
        return answer

if __name__=="__main__":
    Solution.solution()