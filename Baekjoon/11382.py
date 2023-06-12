import sys


class Solution:
    def solution(self):
        a,b,c = map(int, sys.stdin.readline().strip().split(" "))
        print(a+b+c)
        return a+b+c

if __name__ == '__main__':
    s = Solution()
    s.solution()