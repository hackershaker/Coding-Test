def solution(grid):
    answer = set() # frozenset or tuple
    pathset = set() # parts of path
    stack = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            stack.append([((i,j), grid[i][j], (0,1))]) # 위쪽에서 [i,j]를향해 빛이 들어왔다.
            stack.append([((i,j), grid[i][j], (0,-1))]) # 아래쪽에서 [i,j]를향해 빛이 들어왔다.
            stack.append([((i,j), grid[i][j], (-1,0))]) # 왼쪽에서 [i,j]를향해 빛이 들어왔다.
            stack.append([((i,j), grid[i][j], (1,0))]) # 오른쪽에서 [i,j]를향해 빛이 들어왔다.
    # print(stack)
    itercount = 0
    while itercount < 20:
        path = stack.pop()
        print(path)
        if path[-1] in pathset: continue
        node, way, fromin = path[-1]

        nextgrid = nextnode(node, way, fromin)
        if nextgrid == path[0]:
            if frozenset(path) not in answer:
                answer.add(frozenset(path))
                for p in path: pathset.update(path)
        else:
            path.append(nextgrid)
            stack.append(path)

        # print(stack)
        itercount += 1

    return answer

def reflect(node, arrow, grid):
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


# print(solution(	["SL", "LR"] ))