def solution(s):
    answer = ""
    ul = []
    for c in s:
        if c.isupper():
            ul.append([c, 1])
        else:
            ul.append([c, 0])
    ul.sort(key=lambda x: (-x[1], x), reverse=True)
    print(ul)
    for c in ul:
        answer += c[0]
    return answer


print(solution("Zbcdefg"))
