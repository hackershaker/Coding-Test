# 재귀를 이용해 순서 구하고 클래스 변수에 저장

class Solution:
    def __init__(self) -> None:
        self.moveList = []

    def solution(self):
        n = int(input())
        self.moveList = self.move(1,3,n)
        return self.moveList

    def move(self, start: int, end: int, plates: int) -> list:
        if plates == 1: return [[start, end]]
        return self.move(start, 6-start-end, plates-1) + [[start, end]] + self.move(6-start-end, end, plates-1)

if __name__=="__main__":
    s = Solution()
    moveList = s.solution()

    print(len(moveList))
    for s,e in moveList:
        print(str(s) + " " + str(e))