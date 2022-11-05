from collections import deque

def solution():
    n, m = map(int, input().split(" "))
    ground = []

    for _ in range(n):
        ground.append(list(input()))
    # print(n,m,ground)
    answer = 100000

    stack = deque([[(0,0)]])
    visitset = {(0,0)}
    while stack:
        path = stack.popleft()
        if len(path) >= answer: continue
        
        p = path[-1]
        if p == (n-1,m-1):
            answer = min(answer, len(path))
            continue

        u, d, r, l = (p[0]-1, p[1]), (p[0]+1, p[1]), (p[0], p[1]+1), (p[0], p[1]-1)

        for point in u,d,r,l:
            if (point[0] < 0 or point[0] >= n) or (point[1] < 0 or point[1] >= m) or point in visitset or ground[point[0]][point[1]] == "0":
                continue
            stack.append(path + [point])
            visitset.add(point)
    
    return answer

if __name__=="__main__":
    answer = solution()
    print(answer)