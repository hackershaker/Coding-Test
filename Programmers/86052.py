def solution(grid):
    answer = set() # frozenset or tuple
    pathset = set() # parts of path
    stack = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            stack.append([((i,j), (0,1))]) # 오른쪽에서 [i,j]를향해 빛이 들어왔다.
            stack.append([((i,j), (0,-1))]) # 왼쪽에서 [i,j]를향해 빛이 들어왔다.
            stack.append([((i,j), (-1,0))]) # 위쪽에서 [i,j]를향해 빛이 들어왔다.
            stack.append([((i,j), (1,0))]) # 아래쪽에서 [i,j]를향해 빛이 들어왔다.
    # print(stack)
    while stack:
        path = stack.pop()
        if path[-1] in pathset: continue
        # print(path)
        node, way= path[-1]

        nextgrid = reflect(node, way, grid)
        # print("next node : ", nextgrid)
        
        if nextgrid == path[0]:
            if tuple(path) not in answer:
                answer.add(tuple(path)) 
                pathset.update(path)
        else:
            path.append(nextgrid)
            stack.append(path)
    # print(answer)
    return sorted([len(x) for x in answer])

def testsolution(grid):
    testresult = []
    answer = set() # frozenset or tuple
    pathset = set() # parts of path
    stack = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            stack.append([((i,j), (0,1))]) # 오른쪽에서 [i,j]를향해 빛이 들어왔다.
            stack.append([((i,j), (0,-1))]) # 왼쪽에서 [i,j]를향해 빛이 들어왔다.
            stack.append([((i,j), (-1,0))]) # 위쪽에서 [i,j]를향해 빛이 들어왔다.
            stack.append([((i,j), (1,0))]) # 아래쪽에서 [i,j]를향해 빛이 들어왔다.
    # print(stack)
    while stack:
        path = stack.pop()
        if path[-1] in pathset: continue
        node, way= path[-1]

        nextgrid = reflect(node, way, grid)
        if nextgrid == path[0]:
            if tuple(path) not in answer:
                answer.add(tuple(path))
                testresult.append(path)
                pathset.update(path)
        else:
            path.append(nextgrid)
            stack.append(path)

    return testresult

def reflect(node: tuple, arrow: tuple, grid: list):
    nextarrow = None # 받는쪽
    nextnode = None # 빛을 받는 노드
    if grid[node[0]][node[1]] == "L":
        if arrow[1] == 0:
            nextarrow = (-arrow[1], -arrow[0])
            nextnode = validord((node[0]+nextarrow[0], node[1]+nextarrow[1]), grid)
        else:
            nextarrow = (arrow[1], arrow[0])
            nextnode = validord((node[0]-nextarrow[0], node[1]-nextarrow[1]), grid)
    
    if grid[node[0]][node[1]] == "R":
        if arrow[1] == 0:
            nextarrow = (arrow[1], arrow[0])
            nextnode = validord((node[0]+nextarrow[0], node[1]+nextarrow[1]), grid)
        else:
            nextarrow = (-arrow[1], -arrow[0])
            nextnode = validord((node[0]-nextarrow[0], node[1]-nextarrow[1]), grid)

    if grid[node[0]][node[1]] == "S":
        nextarrow = arrow
        nextnode = validord((node[0]-nextarrow[0], node[1]+nextarrow[1]), grid)
        
    return (nextnode, nextarrow)

def validord(point, grid):
    return ( (point[0]+len(grid))%len(grid), (point[1]+len(grid[0]))%len(grid[0]) )

