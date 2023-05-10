import sys


class Solution:
    def __init__(self) -> None:
        self.n, self.m = 0, 0

    def solution(self):
        self.n, self.m, k = map(int, sys.stdin.readline().strip().split(" "))
        phase = sys.stdin.readline().strip()
        board = [list(sys.stdin.readline().strip()) for _ in range(self.n)]

        gravity = {"D": self.down, "U": self.up, "L": self.left, "R": self.right}
        for op in phase:
            board = gravity[op](board)

        for row in board:
            print("".join(row))

        # for row in board:
        #     print("".join(row))

    def right(self, board: list[str]) -> list[str]:
        for i in range(len(board)):
            letters = [element for element in board[i] if element != "."]
            board[i] = ["."] * (len(board[0]) - len(letters)) + letters
        return board

    def left(self, board: list[str]) -> list[str]:
        for i in range(len(board)):
            letters = [element for element in board[i] if element != "."]
            board[i] = letters + ["."] * (len(board[0]) - len(letters))
        return board

    def down(self, board: list[str]):
        arr = self.left(list(map("".join, zip(*board[::-1]))))
        return list(zip(*arr))[::-1]

    def up(self, board):
        arr = self.right(list(map("".join, zip(*board[::-1]))))
        return list(zip(*arr))[::-1]


if __name__ == "__main__":
    s = Solution()
    s.solution()
