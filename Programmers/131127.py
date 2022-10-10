from collections import deque, Counter
def solution(want, number, discount):
    answer = 0
    endidx = 9
    deq = deque(discount[:10])
    deqcount = Counter(deq)
    wantcount = {x[0]:x[1] for x in zip(want, number)}
    while True:
        try:
            print(deqcount, wantcount)
            for w in wantcount:
                if w not in deqcount: break
                else:
                    if deqcount[w] < wantcount[w]: break
            else:
                answer += 1

            el = deq.popleft()
            deqcount[el] -= 1
            if deqcount[el] == 0: deqcount.pop(el, None)
            deq.append(discount[endidx+1])
            if discount[endidx+1] in deqcount.keys(): deqcount[discount[endidx+1]] += 1
            else: deqcount[discount[endidx+1]] = 1
            endidx += 1
        except Exception as e:
            print(e)
            break
    return answer

print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]), 3)