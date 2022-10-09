import math
def solution2(n, edge):
    layer = [[1]]
    edge += [[x[1], x[0]] for x in edge]
    edge.sort(key = lambda x : x[0])
    print(edge)
    exceptnodes = [1]
    while True:
        curlayer = layer[-1]; templayer =[]
        for node in curlayer:
            for line in edge:
                if line[0] == node:
                    pnode, cnode = line[0], line[1]
                    if cnode not in exceptnodes:
                        templayer.append(cnode)
                        exceptnodes.append(cnode)
                    else:
                        continue
                elif line[1] == node:
                    pnode, cnode = line[1], line[0]
                    if cnode not in exceptnodes:
                        templayer.append(cnode)
                        exceptnodes.append(cnode)
                    else:
                        continue
                else:
                    continue

        if templayer == []: break
        layer.append(templayer)
        # print(layer)
    
    answer = len(layer[-1])

    return answer

import math
from collections import deque
def solution(n, edge):
    edge += [[x[1], x[0]] for x in edge]
    graph = {str(x):[] for x in range(1, n+1)}
    minpath = {str(x) : 0 for x in range(1, n+1)}
    for line in edge: graph[str(line[0])].append(line[1])

    # print(minpath)
    path = deque([[1]]); minpath["1"] = 1; maxlen = 0
    while path:
        p = path.popleft()
        # print(p)
        isVaildnode = False
        if graph[str(p[-1])] == None: continue
        for node in graph[str(p[-1])]:
            if minpath[str(node)] == 0:
                # print("first arrived at ", node, " node")
                minpath[str(node)] = len(p)
                # print("min length of ", node, " node is ", len(p) )
                path.append(p + [node])
                maxlen = len(p)
                isVaildnode == True
            elif minpath[str(node)] > len(p):
                # print("shorter path found")
                minpath[str(node)] = len(p)
                # print("min length of ", node, " node is ", len(p) )
                path.append(p + [node])
                isVaildnode == True
            else:
                pass
        
        if ~isVaildnode:
            continue
    
    answer = 0
    minpath.pop("1", None)
    # print(minpath, "maxlen : ",maxlen)
    for p in minpath:
        if maxlen == minpath[p]: answer += 1

    return answer

    
    


# print(solution(	6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]] ), 3)
# print(solution(	5, [[1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5]] ), 4)
# print(solution(	5, [[1, 2], [2, 3], [3, 4], [4, 5]] ), 1)
print(solution(	8, [[1, 2], [1, 3], [1, 4], [2, 3], [3, 4], [2, 5],[3, 6], [4, 7], [5, 6], [6, 7], [7, 5], [6, 8], [8, 5]] ), 1)
# print(solution(	5, [[1, 2], [2, 3], [1, 4], [4, 5]] ))