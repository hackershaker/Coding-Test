def solution(places):
    answer = []
    def checkValid(place):
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    print([i,j])
                    print("#Case1")
                    points = [[i+1, j],[i, j+1],[i-1, j],[i, j-1]]
                    for p in points:
                        if p[0] < 0 or p[0] > 4 or p[1] < 0 or p[1] > 4: continue
                        if place[p[0]][p[1]] == "P":
                            return 0
                    print("#Case2")
                    points = [[i+1, j+1],[i-1, j+1],[i+1, j-1],[i-1, j-1]]
                    for p in points:
                        if p[0] < 0 or p[0] > 4 or p[1] < 0 or p[1] > 4: continue
                        if place[p[0]][p[1]] == "P" and (place[p[0]][j] == "O" or place[i][p[1]] == "O"): return 0
                    print("#Case3")
                    points = [[i+2, j],[i, j+2],[i-2, j],[i, j-2]]
                    for p in points:
                        if p[0] < 0 or p[0] > 4 or p[1] < 0 or p[1] > 4: continue
                        if place[p[0]][p[1]] == "P" and place[int((p[0]+i)/2)][int((p[1]+j)/2)] == "O": return 0
                    
        return 1 


    for place in places:
        answer.append(checkValid(place))
        
    return answer

print(solution(	[["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]] ), [1,0,1,1,1])