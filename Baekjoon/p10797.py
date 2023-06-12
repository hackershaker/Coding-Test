import sys
class Solution:
    def __init__(self):
        self.target = sys.stdin.readline().strip()
        self.number = sys.stdin.readline().strip()
        
    def solution(self):
        print(self.number.count(self.target))


if __name__ == '__main__':
    s = Solution()
    s.solution()