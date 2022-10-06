import ast
from glob import glob


def solution2(m, n, puddles):

    answer = {f"[{n},{m}]": 0}
    memo = {"[1,1]": 1}  # 좌표, 해당 좌표까지 최소경로 갯수
    if puddles != [[]]:
        for i in range(len(puddles)):
            puddles[i] = [puddles[i][1], puddles[i][0]]

    while memo:
        temp = {}
        for cur in memo:
            curord = ast.literal_eval(cur)  # list모양의 string을 list 객체로 바꾸어줌.
            pathnum = memo[cur]

            # move right
            if curord[1] + 1 <= m and [curord[0], curord[1] + 1] not in puddles:
                if [curord[0], curord[1] + 1] == [n, m]:
                    answer[f"[{n},{m}]"] += pathnum
                    continue
                try:
                    temp[str([curord[0], curord[1] + 1])] += pathnum
                except:
                    temp[str([curord[0], curord[1] + 1])] = pathnum
            # move down
            if curord[0] + 1 <= n and [curord[0] + 1, curord[1]] not in puddles:
                if [curord[0] + 1, curord[1]] == [n, m]:
                    answer[f"[{n},{m}]"] += pathnum
                    continue
                try:
                    temp[str([curord[0] + 1, curord[1]])] += pathnum
                except:
                    temp[str([curord[0] + 1, curord[1]])] = pathnum
        # print(temp)
        memo = temp
    length = answer[f"[{n},{m}]"]
    if length < 1000000007:
        return length
    else:
        return length % 1000000007


def solution3(m, n, puddles):
    dic = {}
    if puddles != [[]]:
        for i in range(len(puddles)):
            puddles[i] = [puddles[i][1], puddles[i][0]]

    def getSum(ord):
        import sys

        sys.setrecursionlimit(10 ** 9)

        if ord == [1, 1]:
            dic[str(ord[0]) + str(ord[1])] = 1
            return 1

        pathSum = 0
        # left
        if (
            1 <= ord[0] - 1 <= n
            and 1 <= ord[1] <= m
            and [ord[0] - 1, ord[1]] not in puddles
        ):
            if str(ord[0] - 1) + str(ord[1]) in dic:
                pathSum += dic[str(ord[0] - 1) + str(ord[1])]
            else:
                getSum([ord[0] - 1, ord[1]])
                pathSum += dic[str(ord[0] - 1) + str(ord[1])]

        # up
        if (
            1 <= ord[0] <= n
            and 1 <= ord[1] - 1 <= m
            and [ord[0], ord[1] - 1] not in puddles
        ):
            if str(ord[0]) + str(ord[1] - 1) in dic:
                pathSum += dic[str(ord[0]) + str(ord[1] - 1)]
            else:
                getSum([ord[0], ord[1] - 1])
                pathSum += dic[str(ord[0]) + str(ord[1] - 1)]

        dic[str(ord[0]) + str(ord[1])] = pathSum
        # print(dic)
        return

    getSum([n, m])
    answer = dic[str(n) + str(m)]
    if answer < 1000000007:
        return answer
    else:
        return answer % 1000000007


def solution(m, n, puddles):
    memo = {"1,1": 1}

    i = 3
    while memo:
        for k in range(1, i):
            temp = 0
            if [i - k, k] in puddles:
                memo[str(k) + "," + str(i - k)] = 0
            elif 1 <= k <= n and 1 <= i - k <= m:
                if i - k == 1:
                    memo[str(k) + "," + str(i - k)] = memo[
                        str(k - 1) + "," + str(i - k)
                    ]
                elif k == 1:
                    memo[str(k) + "," + str(i - k)] = memo[
                        str(k) + "," + str(i - k - 1)
                    ]
                else:
                    memo[str(k) + "," + str(i - k)] = (
                        memo[str(k - 1) + "," + str(i - k)]
                        + memo[str(k) + "," + str(i - k - 1)]
                    )

        if i == m + n:
            break
        i += 1

    answer = memo[str(n) + "," + str(m)]
    if answer < 1000000007:
        return answer
    else:
        return answer % 1000000007


print(solution(5, 5, [[2, 2], [2, 3], [2, 4], [3, 2], [4, 2]]))
print(solution(3, 3, [[2, 2]]), 2)
print(solution(3, 3, [[2, 3]]), 3)
print(solution(3, 3, [[1, 3]]), 5)
print(solution(3, 3, [[1, 3], [3, 1]]), 4)
print(solution(3, 3, [[1, 3], [3, 1], [2, 3]]), 2)
print(solution(3, 3, [[1, 3], [3, 1], [2, 3], [2, 1]]), 1)
print(
    solution(7, 4, [[2, 1], [2, 2], [2, 3], [4, 2], [4, 3], [4, 4], [6, 2], [6, 3]]), 0
)  # 이 값이 잘 나오면 테스트1, 테스트9 통과, 위로 가면 안됨
print(solution(4, 4, [[3, 2], [2, 4]]), 7)
print(solution(1, 100, []), 1)
print(solution(2, 2, []), 2)
print(solution(3, 3, []), 6)
print(solution(4, 4, []), 20)
print(solution(5, 5, []), 70)
print(solution(6, 6, []), 252)
print(solution(10, 10, []), 48620)
print(solution(11, 11, []), 184756)
print(solution(11, 12, []), 352716)
print(solution(12, 12, []), 705432)
print(solution(12, 12, [[11, 11]]), 335920)
print(solution(15, 15, []), 40116600)
print(solution(20, 20, []), 345263555)
print(solution(100, 100, []), 690285631)
print(solution(90, 90, []), 322564342)
print(solution(80, 80, []), 731587109)
