def solution(my_string):
    answer = 0
    l = ("+ " + my_string).split(" ")
    print(l)
    for i in range(int(len(l) / 2)):
        if l[2 * i] == "+":
            answer += int(l[2 * i + 1])
        else:
            answer -= int(l[2 * i + 1])
    return answer


print(solution("2 - 4 + 5 - 6 + 4 + 2 + 5 - 8"))
print(solution("10 - 20"))
print(solution("10 + 20 + 100 - 10"))
print(solution("0 + 0 + 0"))
print(solution("10"))
print(solution("3 + 4 + 5"))
print(solution("-100 + 12 + 12"))
