def solution2(numbers):
    answer = []

    for n in numbers:
        count = 0
        nto2 = bin(n)[2:]
        i = n + 1
        a, b = nto2, i
        while len(a) > 0 or b > 0:
            b, rb = divmod(b, 2)
            if len(a) > 0:
                ra = int(a[-1])
                a = a[:-1]
            else:
                ra = 0

            if ra != rb:
                count += 1

            if count > 2:
                i += 1
                a, b, count = nto2, i, 0
                continue

        answer.append(i)

    return answer


import re


def solution(numbers):
    answer = []
    for n in numbers:
        nto2 = "0" + bin(n)[2:]
        print(nto2)
        i = n
        cnt = 0
        if n % 2 == 0 or n % 8 == 1 or n % 8 == 5:
            answer.append(n + 1)
            continue
        elif n % 8 == 3:
            answer.append(n + 2)
            continue
        else:
            l = re.search("0[1]*$", nto2)
            # print(l[0])
            if l != None:
                answer.append(n + 2 ** (len(l[0]) - 2))

        # while True:
        #     i, cnt = i+1, 0
        #     cnt = bin(n^i).count("1")
        #     if cnt <= 2: break

        # answer.append(i)

    return answer


print([7, 15, 23, 31, 39, 47, 55, 63, 71, 79, 87])
print(
    solution([7, 15, 23, 31, 39, 47, 55, 63, 71, 79, 87]),
)
print(solution2([7, 15, 23, 31, 39, 47, 55, 63, 71, 79, 87]))
