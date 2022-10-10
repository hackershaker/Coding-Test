import re
from collections import deque
def solution(user_id, banned_id):
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
    # print(dic)
    
    deq = deque([[] for x in dic[0]])
    i=1
    while True:
        wordset = deq.popleft()
        try:
            for w in dic[len(wordset)]:
                if w not in wordset:
                    deq.append(wordset + [w])
            # print(deq)
        except:
            deq.append(wordset)
            break

    # print(deq)
    answer = set()
    for arr in deq:
        if len(frozenset(arr)) == len(banned_id):
            answer.add(frozenset(arr))
    return len(answer)


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
