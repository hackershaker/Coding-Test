from collections import defaultdict, deque
def solution(n, wires):
    answer = -1; rootnode = wires[0][0]
    wiredic = defaultdict(list)
    net = []; deq = deque(wires)

    while deq:
        wire = deq[0]
        
        if wire[1] in net: 
            wiredic[str(wire[1])].append(wire[0])
            net.extend(wire)
            deq.popleft()
        elif wire[0] in net or len(wiredic) == 0:
            wiredic[str(wire[0])].append(wire[1])
            net.extend(wire)
            deq.popleft()
        else: 
            deq.rotate(-1)

    dic = {}
    def nodecount(n):
        try:
            return dic[str(n)]
        except:
            if wiredic[str(n)] == []:
                dic[str(n)] = 1
                return 1
            else:
                temp = 0
                for node in wiredic[str(n)]:
                    temp += nodecount(node)
                temp += 1
                dic[str(n)] = temp
                return temp

    for i in range(1, n+1):
        nodecount(str(i))
    for key in dic:
        if answer == -1:
            answer = abs(dic[key]*2 - n)
        else:
            answer = min(answer, abs(dic[key]*2 - n))
    return answer

# print(solution(	9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]), 3)
# print(solution(	4, [[1, 2], [2, 3], [3, 4]]), 0)
# print(solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]), 1)
# print(solution(	5, [[1, 2], [1, 3], [1, 4], [1, 5]]), 3)
# print(solution(	8, [[1, 2], [1, 3], [1, 4], [1, 5], [2, 6], [2, 7], [2, 8]]), 0)
# print(solution(	12, [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [5, 7], [1, 9], [2, 10], [3, 11], [4, 12], [10, 8]]), 2)
print(solution(	5, [[1, 2], [2, 4], [3, 5], [4, 3]]), 1)
# print(solution(	13, [[1, 2], [2, 4], [3, 5], [4, 3], [2,8], [4,7], [3,6], [11,12], [12,13], [3,11], [6,9], [10,6]]), 3)