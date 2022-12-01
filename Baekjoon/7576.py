def solution():
    m, n = map(int, input().split(" ")) # n is row, m is column
    ripeTomato, unripeTomato = set(), set()
    box = [list(map(int, input().split(" "))) for _ in range(n)]
    answer = 0

    for i in range(n):
        for j in range(m):
            if box[i][j] == 1:
                ripeTomato.add((i,j))
            elif box[i][j] == 0:
                unripeTomato.add((i,j))
            else: continue

    if len(unripeTomato) == 0: return 0
    
    while True:
        edgeRipeTomato = set()

        for tomato in ripeTomato:
            u,d,r,l = [1,0], [-1,0], [0,1], [0,-1]
            
            for p in u,d,r,l:
                if 0 <= p[0]+tomato[0] < n and 0 <= p[1]+tomato[1] < m and (p[0]+tomato[0], p[1]+tomato[1]) in unripeTomato:
                    edgeRipeTomato.add((p[0]+tomato[0], p[1]+tomato[1]))
                    unripeTomato.remove((p[0]+tomato[0], p[1]+tomato[1]))
        
        answer += 1
        if len(edgeRipeTomato) == 0:
            answer -= 1
            break
        ripeTomato = edgeRipeTomato
        
    if len(unripeTomato) != 0: return -1
    else: return answer

if __name__=="__main__":
    answer = solution()
    print(answer)