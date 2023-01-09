# queue를 이용해 연산 실행


from collections import deque


def solution():
    n, k = map(int, input().split(" "))
    deq = deque([x for x in range(1, n+1)])
    answer = "<"

    while len(deq) > 1:
        deq.rotate(-k+1)
        answer += str(deq.popleft()) + ", "

    answer += str(deq[0]) + ">"

    return answer

if __name__=="__main__":
    answer = solution()
    print(answer)