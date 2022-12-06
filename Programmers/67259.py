from collections import deque
def solution2(board):
    answer = float("inf")

    stack = [ [[(0,0)],0] ]
    while stack:
        path, cost = stack.pop()
        if cost > answer: continue

        p = path[-1]
        if p == (len(board)-1, len(board[0])-1):
            answer = min(answer, cost)

        u,d,r,l = (1,0), (-1,0), (0,1), (0,-1)
        
        for a in d,r,l,u:
            if 0 <= p[0]+a[0] < len(board) and 0 <= p[1]+a[1] < len(board[0]) and (p[0]+a[0], p[1]+a[1]) not in path and board[p[0]+a[0]][p[1]+a[1]] != 1:
                if len(path) == 1:
                    stack.append([path + [(p[0]+a[0], p[1]+a[1])], cost+100])
                else:
                    if path[-2][0]-path[-1][0] == -a[0] and path[-2][1]-path[-1][1] == -a[1]:
                        stack.append([path + [(p[0]+a[0], p[1]+a[1])], cost+100])
                    else:
                        stack.append([path + [(p[0]+a[0], p[1]+a[1])], cost+600])
                    
    return answer

from collections import deque, defaultdict
def solution(board):
    n, m = len(board), len(board[0])
    dic = defaultdict(list)
    dic[(1,0)].append([[(0,0),(1,0)], 100])
    dic[(0,1)].append([[(0,0),(0,1)], 100])
    stack = deque([(1,0),(0,1)])
    while stack:
        node = stack.popleft()
        print(dic[node])
        u,d,r,l = (1,0), (-1,0), (0,1), (0,-1)
        
        for a in d,r,l,u:
            if 0 <= node[0]+a[0] < n and 0 <= node[1]+a[1] < m and board[node[0]+a[0]][node[1]+a[1]] != 1:
                if (node[0]+a[0], node[0]+a[1]) not in dic:
                    stack.append((node[0]+a[0], node[0]+a[1]))
                else:
                    for nextnode in dic[(node[0], node[1])]:
                        path, cost = nextnode[0]

                        if path[-2][0]-path[-1][0] == -a[0] and path[-2][1]-path[-1][1] == -a[1]:
                            dic[(node[0]+a[0], node[1]+a[1])].append([path[-1] + [(node[0]+a[0], node[0]+a[1])], cost+100])
                        else:
                            dic[(node[0]+a[0], node[1]+a[1])].append([path[-1] + [(node[0]+a[0], node[0]+a[1])], cost+600])

    answer = 0
    for total in dic[(n-1, m-1)]:
        answer = min(answer, total)
    return answer