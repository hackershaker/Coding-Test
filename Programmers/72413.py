from collections import deque, defaultdict
import math
# 정확성 테스트 통과, 효율성 시간 초과
def solution(n, s, a, b, fares):
    pathdic = defaultdict(set)
    for info in fares:
        pathdic[(info[0])].add((info[1], info[2]))
        pathdic[(info[1])].add((info[0], info[2]))

    answer = math.inf
    bothminpath = [(-1, None) for x in range(n)]
    bothminpath[s-1] = (0, [s])
    stackbothpath = deque([([s], 0)])
    while stackbothpath: # 같이 간 거리 bfs
        path, curfee = stackbothpath.popleft()
        if pathdic.get((path[-1]), None) == None:
            continue

        for node, fee in pathdic[(path[-1])]:
            if node in path: continue
            if bothminpath[node-1][0] == -1 or bothminpath[node-1][0] > fee + curfee:
                bothminpath[node-1] = (fee + curfee, path+[node])
            stackbothpath.append((path+[node], fee+curfee))

    for bothfee, bothpath in bothminpath:
        if bothpath == None: continue
        toA = returnMinFeePath(bothpath[-1], a, bothpath, pathdic)
        if bothfee + toA >= answer: continue
        toB = returnMinFeePath(bothpath[-1], b, bothpath, pathdic)
        if bothfee + toA + toB < answer:
            answer = bothfee + toA + toB
    return answer

def returnMinFeePath(start, dest, bothpath, dic):
    answer = math.inf
    stack = deque([([start], 0)])
    while stack:
        path, curfee = stack.popleft()
        if path[-1] == dest:
            if curfee < answer:
                answer = curfee
                continue
        for node in dic[(path[-1])]:
            if node[0] in bothpath or node[0] in path or curfee + node[1] >= answer: continue
            stack.append((path+[node[0]], curfee + node[1]))
    return answer

print(solution(	6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]] ))
print(solution( 7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]] ))