import math
def solution(denum1, num1, denum2, num2):
    answer = [denum1*num2/math.gcd(num1,num2) + denum2*num1/math.gcd(num1,num2), num1*num2/math.gcd(num1,num2)]
    answer = list(map(int, answer))
    gcd = math.gcd(answer[0], answer[1])
    answer = [answer[0]/gcd, answer[1]/gcd]
    return answer

print(solution(4,2,4,2))
print(solution(1, 2, 3, 4))
print(solution(1, 3, 1, 3))