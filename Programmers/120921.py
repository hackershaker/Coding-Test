def solution(A, B):
    answer = 1
    temp = A[-1] + A[:-1]
    while temp != B:
        if temp == A: return -1
        temp = temp[-1] + temp[:-1]
        answer += 1 
    return answer % len(A)

print(solution("hello", "ohell"))
print(solution("apple", "elppa"))
print(solution("apple", "pleap"), 3)
print(solution("apple", "apple"), 3)