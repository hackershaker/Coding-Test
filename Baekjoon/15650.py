# bfs 이용하여 수열 제작

from collections import deque


def solution():
    n, m = map(int, input().split(" "))
    sequence = deque([[x] for x in range(1, n+1)])

    while sequence:
        if len(sequence[0]) == m: break
        seq = sequence.popleft()

        for i in range(1, n+1):
            if seq[-1] < i:
                sequence.append(seq+[i])

    return sequence

if __name__=="__main__":
    answer = solution()
    for seqlist in answer:
        print(" ".join(map(str, seqlist)))