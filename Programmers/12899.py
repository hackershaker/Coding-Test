from itertools import product


def solution2(n):
    def getRow(n):
        arr = ["1", "2", "4"]
        if n == 1:
            return arr
        else:
            arr = ["".join(x) for x in product("124", repeat=n)]
            return arr

    def getfloor(n):
        i = 1
        while True:
            s = (3 ** (i + 1) - 1) / 2 - 1
            if s > n:
                break
            elif s == n:
                return int((3 ** (i) - 1) / 2 - 1), i
            else:
                i += 1

        return int((3 ** (i) - 1) / 2 - 1), i

    lastfloorsum, floor = getfloor(n)
    row = getRow(floor)
    return row[n - int(lastfloorsum) - 1]


def solution(n):
    answer = ""
    while n > 0:
        n, r = divmod(n, 3)

        if r == 1:
            answer = "1" + answer
        elif r == 2:
            answer = "2" + answer
        else:
            answer = "4" + answer
            n = n - 1
    return answer


print(solution(32))
