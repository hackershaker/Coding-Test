# deque를 이용해 문제에서 시키는 대로 연산


from collections import deque


def solution():
    n = int(input())

    deck = deque([x for x in range(1, n+1)])

    while len(deck) > 1:
        deck.popleft()
        deck.rotate(-1)

    return deck[0]

if __name__=="__main__":
    print(solution())