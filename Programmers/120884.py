def solution(chicken):
    answer = 0
    while chicken > 9:
        coupon = chicken//10
        answer += chicken//10
        chicken = chicken % 10 + coupon
        # print(chicken)
    return answer

print(solution(100))
print(solution(1081))