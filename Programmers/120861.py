def solution(keyinput: list, board:list) -> list:
    answer = [0,0]
    for arrow in keyinput:
        if arrow == "left" and -int(board[0]/2) <= answer[0]-1 <= int(board[0]/2):
            answer[0] -= 1
        if arrow == "right" and -int(board[0]/2) <= answer[0]+1 <= int(board[0]/2):
            answer[0] += 1
        if arrow == "down" and -int(board[1]/2) <= answer[1]-1 <= int(board[1]/2):
            answer[1] -= 1
        if arrow == "up" and -int(board[1]/2) <= answer[1]+1 <= int(board[1]/2):
            answer[1] += 1
        # print(answer)
    return answer

print(solution(	["left", "right", "up", "right", "right"], [11, 11] ), [2, 1])