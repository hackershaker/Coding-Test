def solution(routes):
    answer = 0
    routes.sort(key=lambda x: (x[0]))

    while routes:
        r = routes.pop()
        dellist = []
        for i in reversed(range(len(routes))):
            if routes[i][1] >= r[0]:
                dellist.append(routes[i])

        answer += 1
        for d in dellist:
            routes.remove(d)

    return answer


print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]), 2)
print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3], [-20, -9], [-12, -3]]), 2)
print(solution([[-2, -1], [1, 2], [-3, 0]]), 2)
print(
    solution(
        [
            [0, 0],
        ]
    ),
    1,
)
print(solution([[0, 1], [0, 1], [1, 2]]), 1)  # 1
print(solution([[0, 1], [2, 3], [4, 5], [6, 7]]), 4)  # 4
print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]), 2)  # 2
print(solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]]), 2)  # 2
print(solution([[-20, 15], [-20, -15], [-14, -5], [-18, -13], [-5, -3]]), 2)  # 2
print(solution([[0, 1], [1, 2], [2, 3], [3, 4]]), 2)
print(solution([[0, 1], [0, 2], [0, 3], [0, 4]]), 1)
print(solution([[0, 1], [0, 2], [0, 3], [1, 4]]), 1)
print(solution([[0, 1], [0, 2], [2, 3], [2, 4]]), 2)
print(solution([[0, 0], [1, 1], [2, 2], [4, 4]]), 4)
print(solution([[0, 1], [0, 1], [0, 2], [2, 3], [2, 4], [1, 2], [-1, 5]]), 2)
