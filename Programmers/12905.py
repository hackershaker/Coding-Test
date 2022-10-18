def solution2(board):
    answer = 0
    dic = {(str(x)+str(y))*2: True if board[x][y] == 1 else False for x in range(len(board)) for y in range(len(board[0]))}
    # print(dic)

    def isSquare(lu, rd):
        try:
            return dic["".join(map(str, lu)) + "".join(map(str, rd))]
        except:
            mid = [int((lu[0] + rd[0])/2), int((lu[1] + rd[1])/2)]
            if (rd[0] - lu[0] + 1) % 2 == 0:
                dic["".join(map(str, lu)) + "".join(map(str, rd))] = isSquare(lu, mid) and isSquare([lu[0], mid[1]+1], [mid[0], rd[1]]) and isSquare([mid[0]+1, lu[1]], [rd[0], mid[1]]) and isSquare([mid[0]+1, mid[1]+1], rd) 
            else:
                temp = isSquare(lu, [rd[0]-1, rd[1]-1]) and isSquare(rd, rd) and any([isSquare([k, rd[1]], [k, rd[1]]) for k in range(lu[0], rd[0])]) and any([isSquare([rd[0], k], [rd[0], k]) for k in range(lu[1], rd[1])])
                dic["".join(map(str, lu)) + "".join(map(str, rd))] = temp
            return dic["".join(map(str, lu)) + "".join(map(str, rd))]

    # print(isSquare([0,0], [1,1]))
    # print(isSquare([0,1], [1,2]))
    # print(isSquare([0,2], [1,3]))
    
    windowsize = 1; maxwdsize = min(len(board), len(board[0]))
    while windowsize <= maxwdsize:
        for i in range(len(board)-windowsize+1):
            for j in range(len(board[0])-windowsize+1):
                # print([i, j], [i+windowsize-1, j+windowsize-1])
                if isSquare([i, j], [i+windowsize-1, j+windowsize-1]):
                    answer = windowsize ** 2
        windowsize += 1

    return answer


def solution(board):
    answer = 0
    dic = {(str(x)+str(y))*2: True if board[x][y] == 1 else False for x in range(len(board)) for y in range(len(board[0]))}
    print(dic)
    def isSquare(lu, rd):
        print(lu, rd)
        try:
            return dic["".join(map(str, lu)) + "".join(map(str, rd))]
        except:
            print(lu, rd)
            if lu[0]!=rd[0] and rd[0]-lu[0] == rd[1]-lu[1]:
                mid = int((rd[0]-lu[0])/2)
                print((lu, [mid, mid]), ([lu[0], mid+1], [mid, rd[1]]), ([mid+1, lu[1]], [rd[0], mid]), ([mid+1, mid+1], rd))
                dic["".join(map(str, lu)) + "".join(map(str, rd))] = isSquare(lu, [mid, mid]) and isSquare([lu[0], mid+1], [mid, rd[1]]) and isSquare([mid+1, lu[1]], [rd[0], mid]) and isSquare([mid+1, mid+1], rd)
            elif rd[0]-lu[0] > rd[1]-lu[1]:
                dic["".join(map(str, lu)) + "".join(map(str, rd))] = isSquare(lu, [lu[0]+ abs(lu[0]-rd[0]) -1, rd[1]]) and isSquare([lu[0]+ abs(lu[0]-rd[0]), lu[1]], rd)
            else:
                dic["".join(map(str, lu)) + "".join(map(str, rd))] = isSquare(lu, [rd[0], rd[1] + abs(lu[1]-rd[1]) -1]) and isSquare([lu[0], rd[1] + abs(lu[1]-rd[1])], rd)
            return dic["".join(map(str, lu)) + "".join(map(str, rd))]

    windowsize = 2; maxwdsize = min(len(board), len(board[0]))
    while windowsize <= maxwdsize:
        for i in range(len(board)-windowsize+1):
            for j in range(len(board[0])-windowsize+1):
                # print([i, j], [i+windowsize-1, j+windowsize-1])
                if isSquare([i, j], [i+windowsize-1, j+windowsize-1]):
                    answer = windowsize ** 2
        windowsize += 1

    return answer

print(solution(	[[0, 0], [1, 1]] ), 1)
print(solution(	[[0, 0, 1, 1], [1, 1, 1, 1]] ), 4)
print(solution(	[[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]] ), 9)