from math import factorial
import sys


class Solution:
    @classmethod
    def bridge(cls):
        T = int(sys.stdin.readline().rstrip())

        for _ in range(T):
            n,m = map(int, sys.stdin.readline().rstrip().split(" "))
            print(int(factorial(m) / (factorial(m-n) * factorial(n))))
    
if __name__=="__main__":
    Solution.bridge()