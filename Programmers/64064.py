import re


def solution(user_id, banned_id):
    answer = []
    dic = [[] for x in banned_id]

    for i in range(len(banned_id)):
        replstr = "^" + banned_id[i].replace("*", "[a-z0-9]") + "$"
        for id in user_id:
            try:
                if re.search(replstr, id)[0] in dic[i]:
                    continue
                dic[i].append(re.search(replstr, id)[0])
            except:
                pass

    # for i in range(len(dic)):
    #     dic[i] = list(set(dic[i]))

    # print(dic)
    def recur(arr):
        if len(arr) == 1:
            return [[x] for x in arr[0]]
        temp = []
        for word in arr[0]:
            for array in recur(arr[1:]):
                if word in array:
                    continue
                else:
                    temp.append([word] + array)
        return temp

    answer = recur(dic)
    # print(answer)

    answerset = []
    for x in answer:
        if set(x) not in answerset:
            answerset.append(set(x))
    # print(answerset)
    return len(answerset)


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]), 2)
print(
    solution(
        ["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]
    ),
    2,
)
print(
    solution(
        ["frodo", "fradi", "crodo", "abc123", "frodoc"],
        ["fr*d*", "*rodo", "******", "******"],
    ),
    3,
)
print(
    solution(
        ["frodo", "fradi", "crodo", "abc123", "frodoc"], ["***d*", "*r*d*", "******"]
    ),
    6,
)
print(solution(["frodo", "fradi", "crodo", "abc12", "frodc"], ["*****"]), 5)
print(solution(["frodo", "fradi", "crodo", "abc12", "frodc"], ["f****", "***d*"]), 6)
print(
    solution(
        ["frodo", "fradi", "crodo", "frido", "abc123", "frodoc", "abc124", "frodic"],
        ["fr*d*", "*rodo", "******", "*****"],
    ),
    30,
)
print(
    solution(
        [
            "aaaaaaaa",
            "bbbbbbbb",
            "cccccccc",
            "dddddddd",
            "eeeeeeee",
            "ffffffff",
            "gggggggg",
            "hhhhhhhh",
        ],
        [
            "********",
            "********",
            "********",
            "********",
            "********",
            "********",
            "********",
            "********",
        ],
    )
)
