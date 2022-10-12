import math
def solution(array, n):
    answer , diff = math.inf, math.inf

    for number in array:
        if abs(number - n) < diff:
            diff = abs(number - n)
            answer = number
        if abs(number - n) == diff:
            answer = min(answer, number)


    return answer

print(solution([3, 10, 28], 20), 28)