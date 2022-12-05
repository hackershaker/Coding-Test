from collections import deque
def solution(board):
    answer = float("inf")

    stack = deque([ [[(0,0)],0] ])
    while stack:
        path, cost = stack.popleft()
        if cost > answer: continue

        p = path[-1]
        if p == (len(board)-1, len(board[0])-1):
            print(p, cost)
            answer = min(answer, cost)
        board[p[0]][p[1]] = 1

        u,d,r,l = (1,0), (-1,0), (0,1), (0,-1)
        
        for a in u,d,r,l:
            if 0 <= p[0]+a[0] < len(board) and 0 <= p[1]+a[1] < len(board[0]) and board[p[0]+a[0]][p[1]+a[1]] != 1:
                if len(path) == 1:
                    stack.append([path[-1:] + [(p[0]+a[0], p[1]+a[1])], cost+100])
                else:
                    if len(path) > 1 and path[-2][0]-path[-1][0] == -a[0] and path[-2][1]-path[-1][1] == -a[1]:
                        stack.append([path[-1:] + [(p[0]+a[0], p[1]+a[1])], cost+100])
                    else:
                        stack.append([path[-1:] + [(p[0]+a[0], p[1]+a[1])], cost+600])
                    
    return answer