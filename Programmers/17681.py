def solution(n, arr1, arr2):
    answer = []

    def convertto2(s):
        s = bin(int(s))[2:]
        s = (n - len(s)) * "0" + s
        return s

    for x, y in zip(arr1, arr2):
        x, y = convertto2(x), convertto2(y)
        print(x, y)
        temp = ""
        for a, b in zip(x, y):
            if int(a) or int(b):
                temp += "#"
            else:
                temp += " "
        answer.append(temp)

    return answer


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
