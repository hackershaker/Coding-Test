from collections import deque
def solution2(queue1, queue2):
    answer = 0
    snapshot = []
    q1, q2 = deque(queue1), deque(queue2)
    avg = int((sum(q1) + sum(q2)) / 2)
    while sum(q1) != avg or sum(q2) != avg:
        if sum(q1) > sum(q2):
            q2.append(q1.popleft())
        else:
            q1.append(q2.popleft())
        print(q1, q2)
        answer += 1

        if (list(q1), list(q2)) not in snapshot: snapshot.append((list(q1), list(q2)))
        else:
            answer = -1
            break
        # print(snapshot)
        # if list(q1) == queue1:
        #     answer = -1
        #     break
    
    # print(q1, q2)
    return answer

from collections import deque
import math
def solution(queue1, queue2): # two pointer
    answer = math.inf
    len1, len2 = len(queue1), len(queue2)
    queue1.extend(queue2) # [3,2,7,2,4,6,5,1] 작업횟수 4번

    start , end = 0, 0
    if sum(queue1) % 2 == 1: return -1
    avg = int(sum(queue1)/2)
    found = False
    deq = deque([queue1[0]]); deqsum = queue1[0]
    while True:
        # print(deq, start, end)
        if end == len(queue1)-1: break

        if deqsum < avg:
            deq.append(queue1[end+1])
            deqsum += queue1[end+1]
            end += 1
        elif deqsum > avg:
            el = deq.popleft()
            deqsum -= el
            start += 1
        else:
            found = True
            k = start + end - len1 + 1
            if end < len1-1:
                answer = min(answer, len2 + end + 1)
            else:
                answer = min(answer, k)
            # print(answer)
            deq.append(queue1[end+1])
            deqsum += queue1[end+1]
            end += 1
    if found: return answer
    else: return -1 


# print(solution( [3, 2, 7, 2], [4, 6, 5, 1]), 2)
# print(solution( [2, 7, 2], [4, 6, 5, 1, 3]), 1)
print(solution( [2, 7, 2, 4], [6, 5, 1, 3]), 0)
print(solution( [7, 2, 4], [6, 5, 1, 3, 2]), 4)
print(solution( [7, 2, 4, 6], [5, 1, 3, 2]), 3)
print(solution( [2, 4, 6], [5, 1, 3, 2, 7]), 2)
print(solution( [2, 4, 6, 5], [1, 3, 2, 7]), 1)
print(solution( [4, 6, 5], [1, 3, 2, 7, 2]), 0)
print(solution( [4, 6, 5, 1], [3, 2, 7, 2]), 2)
print(solution( [4, 6, 5, 1, 3], [2, 7, 2]), 1)
print(solution( [6, 5, 1], [3, 2, 7, 2, 4]), 1)

print(solution( [1, 2, 3, 4], [2, 1, 4, 3]), 0)
print(solution( [1, 2, 3, 4, 2], [1, 4, 3]), 3)

# print(solution( [1], [2]), -1)
# print(solution(	[1, 1], [1, 5]), -1)
# print(solution(	[1, 1, 1], [5, 5, 5]), -1)
# print(solution(	[1, 2, 3], [4, 5, 7]), -1)
# print(solution(	[3, 4, 5], [2, 4, 8]), -1)

# print(solution( [3, 4, 7, 2], [4, 6, 3, 1]), 2)
# print(solution( [2, 1], [1,2,3,4,5]), 3)
# print(solution( [1, 1], [2,2,1,1,1,10,1]), 13)
# print(solution(	[1, 2, 1, 2], [1, 10, 1, 2]), 7)
