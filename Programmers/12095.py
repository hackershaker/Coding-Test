def solution2(board):
    answer = 0
    maxsize = min(len(board), len(board[0]))
    windowsize = maxsize


    while windowsize:
        for i in range(maxsize-windowsize+1):
            # print(windowsize, i)
            # print(board[i: windowsize+i])
            temp = board[i: windowsize+i]
            total = 0
            for j in range(len(board[0])-windowsize+1):
                total = 0
                for arr in temp:
                    # print(arr[j:j+windowsize])
                    total += sum(arr[j:j+windowsize])
                if total == windowsize ** 2: return total
                # print("=======================")

        windowsize -= 1

    return answer

def solution3(board):
    answer = 1

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                continue
            else:
                windowsize = 1
                squareExists = True
                while squareExists:
                    for ordx, ordy in [[a, b] for a in range(i, i+windowsize) for b in range(j, j+windowsize)]:
                        # print(ordx, ordy)
                        if ordx >= len(board) or ordy >= len(board[0]) or board[ordx][ordy] != 1:
                            squareExists = False
                            break
                    else:
                        squareExists = True
                        # print(f"found square, size is {windowsize}, startpoint is {i, j}")
                        answer = max(answer, windowsize ** 2)
                        windowsize += 1

    return answer

def solution4(board): # 효율성에서 떨어짐
    answer = 1
    list1 = [[i, j] for i in range(len(board)) for j in range(len(board[0])) if board[i][j] == 1]
    list0 = [[i, j] for i in range(len(board)) for j in range(len(board[0])) if board[i][j] == 0]
    
    if len(list1) == 0: return 0

    for ordinate in list1:
        i, j = ordinate
        winsize = 2
        squareexists= True
        # print(i, j)
        while squareexists:
            if i + winsize -1 >= len(board) or j + winsize -1 >= len(board[0]):
                # print("invalid size")
                break
            for zeroord in list0:
                # print("zero in square", zeroord)
                if i <= zeroord[0] <= i + winsize -1 and j <= zeroord[1] <= j + winsize -1: 
                    squareexists = False
                    break
            else:
                # print(f"found square size {winsize}")
                answer = max(answer, winsize ** 2)
                winsize += 1

    return answer

from collections import deque
def solution(board):
    answer = 1
    squares = [[[i, j]] * 4 for i in range(len(board)) for j in range(len(board[0])) if board[i][j] == 1] # lu, ru, ld, rd
    deq = deque(squares)
    # print(squares)
    dic = {"".join(map(str, x[0])) + "," +"".join(map(str, x[3])): 1 for x in squares}
    # print(dic)

    while deq:
        square = deq.popleft()
        lu, ru, ld, rd = square
        # print(lu, ru, ld, rd)
        if rd[1] + 1 > len(board[0])-1 or rd[0] + 1 > len(board)-1 or [rd[0] + 1, rd[1] + 1] == 0:
            answer = max(answer, (ru[1]-lu[1]+1) ** 2 )
            # print(answer)
            continue

        temp = 0
        for i in range(ru[1]-lu[1]+1):
            # print(i, ru, ld)
            temp += board[ru[0]+i][ru[1]+1] + board[ld[0]+1][ld[1]+i]
        temp += board[rd[0]+1][rd[1]+1]

        try:
            total = dic["".join(map(str, lu)) + "," + "".join(map(str, rd))] + temp
            if total != (ru[1]-lu[1]+2) ** 2:
                continue
            else:
                answer = max(answer, total)
                deq.append([lu, [ru[0], ru[1]+1], [ld[0]+1, ld[1]], [rd[0]+1, rd[1]+1]])
            dic["".join(map(str, lu)) + "," + "".join(map(str, [rd[0]+1, rd[1]+1]))] = total
        except:
            continue

    return answer


print(solution(	[[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]), 9)
print(solution(	[[0, 0, 1, 1], [1, 1, 1, 1]]), 4)
print(solution(	[[1,1,1,1]]), 1)
print(solution(	[[1]*100]*100), 1000000)
print(solution(	[[1]*200]*200), 1000000)