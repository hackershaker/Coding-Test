from collections import deque
import math
def solution(N, road, K):
    answer = 0
    minlen = [0] + [math.inf] * (N-1)
    road += [[x[1], x[0], x[2]] for x in road]
    # print(road)
    matrix = [[0]*N for _ in range(N)] 
    for r in road:
        if matrix[r[0]-1][r[1]-1] == 0: matrix[r[0]-1][r[1]-1] = r[2]
        else: matrix[r[0]-1][r[1]-1] = min(matrix[r[0]-1][r[1]-1], r[2])

    # print(matrix)
    
    stack = deque([[[1], 0]])
    while stack:
        p = stack.popleft()
        # print(p)
        if p[1] > K:
            minlen[p[0][-1]-1] = min(minlen[p[0][-1]-1], K+1)
            continue
        for i in range(N):
            if i+1 in p[0]: continue
            elif matrix[p[0][-1]-1][i] == 0: continue
            elif p[1] + matrix[p[0][-1]-1][i] > minlen[i]: continue
            else:
                stack.append([p[0] + [i+1], p[1] + matrix[p[0][-1]-1][i]])
                minlen[i] = min(p[1] + matrix[p[0][-1]-1][i], minlen[i])
        # print(minlen)
    # print(minlen)
    answer = [x for x in minlen if x <= K]
    return len(answer)


print(solution(	5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3 ), 4)