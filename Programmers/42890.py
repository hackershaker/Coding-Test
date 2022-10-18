from itertools import combinations


def solution(relation):
    answer = []

    for i in range(1, len(relation[0]) + 1):
        for c in combinations(range(len(relation[0])), i):
            if any(candkey | set(c) == set(c) for candkey in answer):
                continue
            colset = set()
            for x in relation:
                temp = []
                for idx in c:
                    temp.append(x[idx])
                colset.add(",".join(temp))

            if len(colset) == len(relation):
                # answer.append("".join(map(str, c)))
                answer.append(set(c))
    print(answer)
    return len(answer)


print(
    solution(
        [
            ["100", "ryan", "music", "2"],
            ["200", "apeach", "math", "2"],
            ["300", "tube", "computer", "3"],
            ["400", "con", "computer", "4"],
            ["500", "muzi", "music", "3"],
            ["600", "apeach", "music", "2"],
        ]
    )
)

print(
    solution(
        [
            ["100", "ryan", "music", "2", "a"],
            ["200", "apeach", "math", "2", "b"],
            ["300", "tube", "computer", "3", "b"],
            ["400", "con", "computer", "4", "b"],
            ["500", "muzi", "music", "3", "c"],
            ["600", "apeach", "music", "2", "d"],
        ]
    )
)

print(
    solution(
        [
            ["100", "ryan", "music"],
            ["200", "ryan", "math"],
            ["300", "ryan", "computer"],
            ["400", "ryan", "tennis"],
            ["500", "ryan", "sf"],
            ["500", "apeach", "english"],
        ]
    )
)
print(
    solution(
        [
            ["100", "ryan", "music", "2", "a"],
            ["200", "apeach", "math", "2", "b"],
            ["300", "tube", "computer", "3", "b"],
        ]
    )
)
print(
    solution(
        [
            ["200", "ryan", "computer"],
            ["200", "spicon", "math"],
            ["300", "ryan", "computer"],
            ["300", "ryan", "tennis"],
            ["400", "ryan", "sf"],
            ["400", "apeach", "tennis"],
        ]
    )
)
