# need testcode

if __name__=="__main__":
    n, m = map(int, input().split(" "))
    ground = []

    for _ in range(n):
        ground.append(list(input()))
    
    answer = 10000

    stack = [[(0,0)]]
    while stack:
        path = stack.pop()
        if len(path) >= answer: continue
        
        p = path[-1]
        if p == (n-1,m-1):
            answer = min(answer, len(path))
            continue

        ground[p[0]][p[1]] = 0

        u, d, r, l = (p[0]-1, p[1]), (p[0]+1, p[1]), (p[0], p[1]+1), (p[0], p[1]-1)

        for point in u,d,r,l:
            if (point[0] < 0 or point[0] >= n) or (point[1] < 0 or point[1] >= m) or ground[point[0]][point[1]] == 0:
                continue
            else:
                stack.append(path + [point])