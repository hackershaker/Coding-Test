def solution(genres, plays):
    answer = []
    genredic = {x: [] for x in set(genres)}
    for g, p in zip(genres, enumerate(plays)):
        genredic[g].append(p)

    genredic = sorted(
        genredic.items(), key=lambda item: -list(map(sum, zip(*item[1])))[1]
    )
    print(genredic)

    for item in genredic:
        l = item[1]
        l.sort(key=lambda x: x[1], reverse=True)
        for song in l[:2]:
            answer.append(song[0])
    return answer


print(
    solution(
        ["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]
    )
)
