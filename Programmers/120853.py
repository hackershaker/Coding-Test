def solution(s):
    stack = []
    s = s.split(" ")
    for i in range(len(s)):
        if s[i] == "Z":
            stack.pop()
        else:
            stack.append(int(s[i])) 

    return sum(stack)

print(solution("5 10 Z 6 20 Z 1 3"))
print(solution("-5 -5 -1 -5 -5 -5 1 Z"))
print(solution("Z 2"))
print(solution("Z 1 Z"))
print(solution("1 2 3 Z 1 Z"))