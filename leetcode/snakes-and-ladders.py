# bfs 이용


from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        answer = float("inf")
        stack = deque([(1,0,)]); n = len(board); nSquare = n ** 2
        dic = {x: float("inf") for x in range(1, nSquare) }
        dic[1] = 0
        while stack:
            curr, move = stack.popleft()
            if curr >= nSquare:
                answer = min(answer , move)
                continue
            if move > dic[curr]: continue
            dic[curr] = move
            # print("Current location :", curr, "Current Move :", move)

            canReachLocation = 0
            for i in range(1, min(6, nSquare - curr)+1):
                x,y = Solution.convertOrd(curr + i, n)
                #ladder
                if board[x][y] > curr+i:
                    # print(f"Ride ladder, from {curr+i} move to {board[x][y]}")
                    stack.append((board[x][y], move+1,))
                #can arrive with dice roll
                if board[x][y] == -1:
                    canReachLocation = curr + i
                #snake
                if 1 < board[x][y] < curr+i:
                    # print(f"Ride Snake from {curr+i} move to {board[x][y]}")
                    stack.append((board[x][y], move+1,))

            if canReachLocation != 0:
                stack.append((min(canReachLocation, nSquare), move+1,))
                        
        return -1 if answer == float("inf") else answer
    
    @staticmethod
    def convertOrd(x, n):
        m, r = divmod(x-1, n)
        return (n-1 - m, r if m % 2 == 0 else n-1 - r)
