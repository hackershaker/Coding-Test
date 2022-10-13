from collections import deque
def solution(order):
    answer = 0
    container = deque([i for i in range(1, len(order)+1)])
    sideContainer = []
    order = deque(order)
    targetbox = order.popleft()
    while targetbox != None:
        if container and container[0] == targetbox:
            answer += 1
            container.popleft()
            targetbox = order.popleft() if order else None
            continue

        if sideContainer and sideContainer[-1] == targetbox:
            answer += 1
            sideContainer.pop()
            targetbox = order.popleft() if order else None
            continue
        
        if container:
            sideContainer.append(container.popleft())
        
        if len(container) == 0 and sideContainer[-1] != targetbox: break

    return answer

print(solution(	[4, 3, 1, 2, 5]), 2)
print(solution([5, 4, 3, 2, 1]), 5)
print(solution([1, 2, 3, 4, 5]), 5)
print(solution([1]), 1)
print(solution([5,1,4,2,3]), 1)
print(solution([2,3,4,5,1]), 5)
print(solution([4,3,2,1,5]), 5)