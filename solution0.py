# 효율성 테스트 모두 실패함
def solution2(maps):
    answer = 0
    distance = [float("inf")]

    def explore(cur, path):
        targetpathlist = [
            [cur[0] - 1, cur[1]],
            [cur[0] + 1, cur[1]],
            [cur[0], cur[1] - 1],
            [cur[0], cur[1] + 1],
        ]
        if len(path) >= distance[0]:
            return

        for k in targetpathlist:
            if not (1 <= k[0] <= len(maps)) or not (1 <= k[1] <= len(maps[0])):
                continue
            elif k in path:
                continue
            elif maps[k[0] - 1][k[1] - 1] == 0:
                continue

            # elif not ( (abs(path[-1][0] - k[0]) == 1 and path[-1][1] - k[1] == 0) or (abs(path[-1][1] - k[1]) == 1 and path[-1][0] - k[0] == 0) ):
            #     continue
            elif k[0] == len(maps) and k[1] == len(maps[0]):
                if len(path) + 1 < distance[0]:
                    distance[0] = len(path) + 1
                else:
                    return
            else:
                explore(k, path + [k])
                continue

        return

    explore([1, 1], [[1, 1]])
    if distance[0] == float("inf"):
        return -1
    else:
        answer = distance[0]

    return answer


from collections import deque


def solution(maps):
    answer = 0
    n, m = len(maps), len(maps[0])

    path = deque([[[1, 1]]])
    visited = [[1, 1]]

    for map in maps:
        if 0 in map:
            break
    else:
        return n + m - 1

    while path:
        p = path.popleft()
        u, d, l, r = (
            [p[-1][0] - 1, p[-1][1]],
            [p[-1][0] + 1, p[-1][1]],
            [p[-1][0], p[-1][1] - 1],
            [p[-1][0], p[-1][1] + 1],
        )
        if n >= u[0] >= 1 and m >= u[1] >= 1:
            if u == [n, m]:
                answer = len(p) + 1
                break
            if maps[u[0] - 1][u[1] - 1] != 0 and u not in visited:
                path.append(p + [u])
                visited.append(u)
        if n >= d[0] >= 1 and m >= d[1] >= 1:
            if d == [n, m]:
                answer = len(p) + 1
                break
            if maps[d[0] - 1][d[1] - 1] != 0 and d not in visited:
                path.append(p + [d])
                visited.append(d)
        if n >= l[0] >= 1 and m >= l[1] >= 1:
            if l == [n, m]:
                answer = len(p) + 1
                break
            if maps[l[0] - 1][l[1] - 1] != 0 and l not in visited:
                path.append(p + [l])
                visited.append(l)
        if n >= r[0] >= 1 and m >= r[1] >= 1:
            if r == [n, m]:
                answer = len(p) + 1
                break
            if maps[r[0] - 1][r[1] - 1] != 0 and r not in visited:
                path.append(p + [r])
                visited.append(r)

    return answer if answer > 0 else -1


# print([[0]*99 + [1]])
array1 = (
    [[1] * 100]
    + [[0] * 99 + [1]]
    + [[1] * 100 for _ in range(1, 97)]
    + [[1] + [0] * 99]
    + [[1] * 100]
)
print(solution(array1))
