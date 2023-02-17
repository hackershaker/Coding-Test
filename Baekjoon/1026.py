import sys


class Solution:
    def solution(self):
        n = int(sys.stdin.readline().rstrip())

        a = list(map(int, sys.stdin.readline().rstrip().split(" ")))
        b = list(map(int, sys.stdin.readline().rstrip().split(" ")))

        a.sort()
        b.sort(reverse=True)

        answer = sum([x*y for x,y in zip(a,b)])
        print(answer)
        return answer

if __name__=="__main__":
    s = Solution()
    s.solution()