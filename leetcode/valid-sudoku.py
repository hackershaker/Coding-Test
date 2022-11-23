from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            num = "".join(row).replace(".", "")
            if len(num) != len(set(num)):
                return False

        for column in zip(*board):
            num = "".join(column).replace(".", "")
            if len(num) != len(set(num)):
                return False

        for i in range(3):
            for j in range(3):
                temp = board[3*i][3*j:3*j+3]+board[3*i+1][3*j:3*j+3]+board[3*i+2][3*j:3*j+3]
                num = "".join(temp).replace(".","")
                if len(num) != len(set(num)):
                    return False

        return True