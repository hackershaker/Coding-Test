def solution(quiz):
    answer = []
    for q in quiz:
        q = q.split(" ")
        value = 0; sign = 1
        nextsign = 1
        for i in range(len(q)):
            if q[i].isnumeric():
                value += int(q[i]) * nextsign * sign
                nextsign = 1
            elif q[i][0] == '-' and q[i][1:].isnumeric():
                value -= int(q[i][1:]) * nextsign * sign
                nextsign = 1
            elif q[i] == '-':
                nextsign = -1
            elif q[i] == "=":
                sign = -1
            else:
                pass
        if value==0: answer.append("O")
        else: answer.append("X")
    return answer

print(solution(["3 - 4 = -3", "5 + 6 = 11"]))
print(solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]))