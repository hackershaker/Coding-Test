from collections import deque


class Solution:
    def __init__(self):
        self.n, self.m, self.x, self.y, self.k = map(int, input().split(" "))
        self.board = [list(map(int, input().split(" "))) for _ in range(self.n)]
        self.dice = {
            "r": deque([0, 0, 0, 0]),  # top,right,bottom,left
            "c": deque([0, 0, 0, 0]),  # top,up,bottom,down
        }
        self.answer = []

    def solution(self):
        commands = input().split(" ")
        for command in commands:
            a, b = self.x, self.y
            if command == "1":
                b += 1
            if command == "2":
                b -= 1
            if command == "3":
                a -= 1
            if command == "4":
                a += 1
            if 0<=a<self.n and 0<=b<self.m:
                self.x,self.y =a,b
                self.diceroll(command)
                if self.board[a][b] == 0:
                    self.board[a][b] = self.dice["r"][2]
                else:
                    self.dice["r"][2] = self.board[a][b]
                    self.board[a][b] = 0
                self.answer.append(self.dice["r"][0])
        
        for ans in self.answer:
            print(ans)


    def diceroll(self, command):
        if command == "1":
            self.dice["r"].rotate(1)
        if command == "2":
            self.dice["r"].rotate(-1)
        self.dice["c"][0], self.dice["c"][2] = self.dice["r"][0], self.dice["r"][2]

        if command == "3":
            self.dice["c"].rotate(1)
        if command == "4":
            self.dice["c"].rotate(-1)
        self.dice["r"][0], self.dice["r"][2] = self.dice["c"][0], self.dice["c"][2]


if __name__ == "__main__":
    s = Solution()
    s.solution()
