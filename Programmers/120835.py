def solution(emergency):
    emergencysort = sorted(emergency, reverse=True)
    dic = {str(emergencysort[i]): i + 1 for i in range(len(emergency))}

    answer = []
    for e in emergency:
        answer.append(dic[str(e)])
    return answer


print(solution([3, 76, 24]))
print(solution([1, 2, 3, 4, 5, 6, 7]))
print(solution([30, 10, 23, 6, 100]))
