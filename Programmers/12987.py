def solution2(A, B):
    answer = 0

    B.sort()
    for a in A:
        for b in B:
            if a < b:
                answer += 1
                B.remove(b)
                break

    return answer


from collections import deque


def solution(A, B):

    answer = 0

    A, B = deque(sorted(A)), deque(sorted(B))
    k = 0
    rot = 0
    while rot <= len(A):
        if len(A) == 0 or len(B) == 0:
            break
        if A[0] < B[0]:
            answer += 1
            A.popleft()
            B.popleft()
            rot = 0
        else:
            B.rotate(-1)
            rot += 1
        k += 1

    return answer


print(solution([5, 1, 3, 7], [2, 2, 6, 8]))
print(solution([2, 2, 2, 2], [1, 1, 1, 1]))
print(solution([1, 2, 3, 4], [5, 6, 7, 8]))
print(solution([1], [1]))
