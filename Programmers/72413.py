from collections import deque, defaultdict

def solution(n, s, a, b, fares):
    pathdic = defaultdict(set)
    for info in fares:
        pathdic[(info[0])].add((info[1], info[2]))
        pathdic[(info[1])].add((info[0], info[2]))
    
    answer = -1
    bothminpath = [(-1, None) for x in range(n)]
    bothminpath[s-1] = (0, [s])
    stackbothpath = deque([([s], 0)])
    visitedbothpath = []
    while stackbothpath: # 같이 간 거리 bfs
        path, curfee = stackbothpath.popleft()
        if pathdic.get((path[-1]), None) == None:
            continue

        for node, fee in pathdic[(path[-1])]:
            if node in path: continue
            if bothminpath[node-1][0] == -1 or bothminpath[node-1][0] > fee + curfee:
                bothminpath[node-1] = (fee + curfee, path+[node])
            stackbothpath.append((path+[node], fee+curfee))

    print(bothminpath)
    return answer

def returnMinFeePath(start, dest):
    return 1

print(solution(	6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]] ))