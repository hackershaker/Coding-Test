from collections import defaultdict, deque, Counter
def solution(topping):
    answer = 0
    a, b = deque([]), deque(topping)
    cb = Counter(b)
    ca = defaultdict(int)

    while b:
        print(ca, cb)
        el = b.popleft()
        cb[el] -= 1
        if cb[el] == 0:
            del cb[el]
        a.append(el)
        ca[el] += 1

        if len(ca) == len(cb): answer += 1
        
    return answer

print(solution([1, 2, 1, 3, 1, 4, 1, 2]), 2)
print(solution([1, 2, 3,1,4]), 0)