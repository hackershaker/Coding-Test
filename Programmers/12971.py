from heapq import heappop, heappush
from itertools import count


def solution(sticker):
    answer = 0
    heap = []
    entryFinder = {}
    counter = count()
    REMOVED = "<removed-task>"

    for i in range(len(sticker)):
        id = next(counter)
        heappush(
            heap, [sticker[i - 1] + sticker[(i + 1) % len(sticker)], -sticker[i], i, id]
        )
        entryFinder[i] = [id, '']

    while heap:
        # print(heap)
        # print(entryFinder)
        entry = heappop(heap)
        if entryFinder[entry[2]][-1] == REMOVED:
            continue
        
        answer -= entry[1]  
        idx = entry[2]
        sticker[idx - 1], sticker[idx], sticker[(idx + 1) % len(sticker)] = 0, 0, 0
        entryFinder[idx][-1] = REMOVED
        (
            entryFinder[(idx - 1 + len(sticker)) % len(sticker)][-1],
            entryFinder[(idx + 1) % len(sticker)][-1],
        ) = (REMOVED, REMOVED)
        (
            entryFinder[(idx - 2 + len(sticker)) % len(sticker)][-1],
            entryFinder[(idx + 2) % len(sticker)][-1],
        ) = (REMOVED, REMOVED)

        if sticker[idx-2] != 0:
            id = next(counter)
            heappush(
                heap, [sticker[idx - 3] + sticker[idx - 1], -sticker[idx - 2], (idx - 2 + len(sticker)) % len(sticker), id]
            )
            entryFinder[(idx - 2 + len(sticker)) % len(sticker)] = [id, '']

        if sticker[(idx + 2) % len(sticker)] != 0:
            id = next(counter)
            heappush(
                heap,
                [
                    sticker[(idx + 1) % len(sticker)] + sticker[(idx + 3) % len(sticker)],
                    -sticker[(idx + 2) % len(sticker)],
                    (idx + 2) % len(sticker),
                    id,
                ],
            )
            entryFinder[(idx + 2) % len(sticker)] = [id, '']

    return answer
