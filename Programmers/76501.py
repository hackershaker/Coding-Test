def solution(absolutes, signs):
    answer = 0
    sign = {True: 1, False: -1}
    for n, s in zip(absolutes, signs):
        print(s, n)
        answer += n * sign[s]
    return answer


print(solution([4, 7, 12], [True, False, True]))
