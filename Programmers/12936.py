from math import factorial
def solution(n, k):
    num = [x for x in range(1, n+1)]
    answer = []
    for i in range(n, 1, -1):
        j = (k-1) // factorial(i-1)
        # print(j-1)
        answer.append(num[j])
        del num[j]
        # print(num)
        k = k % factorial(i-1)
        # print(k)
    answer.append(num[0])
    return answer

print(solution(3,5))
print(solution(4,1))
print(solution(4,2))
print(solution(4,3))
print(solution(4,4))
print(solution(4,5))
print(solution(4,6))
print(solution(4,9))