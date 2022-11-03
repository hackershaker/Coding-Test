from sys import prefix
import numpy as np
from pprint import pprint
def solution2(board, skill):
    answer = 0
    board = np.array(board)
    
    for info in skill:
        board[info[1]:info[3]+1, info[2]:info[4]+1] = board[info[1]:info[3]+1, info[2]:info[4]+1] + score(info[0], info[5])

    return len(board[board > 0])

def solution(board, skill):
    prefixsum = [[0 for _ in range((len(board[0])+1))] for _ in range((len(board)+1))] 
    
    for info in skill:
        r1, c1, r2, c2 = info[1], info[2], info[3], info[4]
        num = score(info[0], info[5])
        prefixsum[r1][c1] += num
        prefixsum[r1][c2+1] += -num
        prefixsum[r2+1][c1] += -num
        prefixsum[r2+1][c2+1] += num

    for k in range(len(prefixsum)):
        for i in range(1, len(prefixsum[k])):
            prefixsum[k][i] += prefixsum[k][i-1]
        

    for k in range(len(prefixsum)):   
        if k != 0:
            prefixsum[k] = list(map(sum, zip(prefixsum[k], prefixsum[k-1])))

    answer = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]+prefixsum[i][j] > 0:
                answer += 1
    return answer

def score(type, degree):
    if type==1:
        return -degree
    else:
        return degree

print(solution(	[[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]], [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]), 10)
print(solution(	[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]]), 6)