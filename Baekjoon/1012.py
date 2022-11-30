def solution() -> list:
    T = int(input())
    answerlist = []

    for _ in range(T):
        answer = 0
        m, n, k = map(int, input().split(" "))
        cabbages = [list(map(int, input().split(" "))) for _ in range(k)]
        testPoint = set()

        for i in range(m):
            for j in range(n):
                if (i,j) in testPoint: continue
                if cabbages[i][j] == 1:
                    stack = {(i,j)}
                    while stack:
                        point = stack.pop()
                        testPoint.add(point)
                        u,d,r,l = [1,0], [-1,0], [0,1], [0,-1]
                        for p in u,d,r,l:
                            x = point[0]+p[0]
                            y = point[1]+p[1]
                            if 0 <= x < m and 0 <= y < m and cabbages[x][y] == 1 and (x,y) not in stack:
                                stack.add((x,y))
                    answer += 1
        
        answerlist.append(answer)

    return answerlist

if __name__=="__main__":
    answer = solution()
    for worm in answer:
        print(worm)