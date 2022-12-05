def solution():
    n, m = map(int, input().split(" "))
    board = [input() for _ in range(n)]
    row = ['WBWBWBWB', 'BWBWBWBW']
    answer = float("inf")

    for i in range(n-7):
        for j in range(m-7):
            wSideWrong, BsideWrong = 0, 0
            for k in range(8):
                for l in range(8):
                    if board[i+k][j+l] != row[(i+k)%2][l]: wSideWrong += 1
                    if board[i+k][j+l] != row[(i+k+1)%2][l]: BsideWrong += 1
            answer = min(answer, wSideWrong, BsideWrong)

    return answer

if __name__=="__main__":
    answer = solution()
    print(answer)