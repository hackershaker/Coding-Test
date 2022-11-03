def solution(n):
    possible = set()

    def explore(ords, board):
        stack = [[ords, board]]
        while stack:
            path, brd = stack.pop()
            if len(path)==n:
                possible.add(frozenset(path))
                continue
                
            targetrow = path[-1][0]+1
            deleteset = makeDelSet(path, n)
            
            leftnodes = brd - deleteset
            if len(leftnodes) == 0: continue
            for x in leftnodes:
                if x[0] == targetrow:
                    stack.append([path+[x], leftnodes])
    
    for i in range(n):
        explore([(0,i)], {(x,y) for x in range(n) for y in range(n)})

    return len(possible)

def makeDelSet(path, n):
    deleteset = set()

    for i in range(1, path[-1][1]+1):
        deleteset.add((path[-1][0], path[-1][1]-i))
    for i in range(1, n - path[-1][1]):
        deleteset.add((path[-1][0], path[-1][1]+i))
    for i in range(1, n-path[-1][0]):
        deleteset.add((path[-1][0]+i, path[-1][1]))
    for i in range(1, min(path[-1][1]+1, n-path[-1][0])):
        deleteset.add((path[-1][0]+i, path[-1][1]-i))
    for i in range(1, min(n - path[-1][0], n-path[-1][1])):
        deleteset.add((path[-1][0]+i, path[-1][1]+i))
    return deleteset
    
print(solution(2), 0)
print(solution(3), 0)
print(solution(4), 2)
print(solution(5), 10)
print(solution(6), 4)
print(solution(7), 40)
print(solution(8), 92)
print(solution(9), 352)
print(solution(10), 724)
print(solution(11), 2680)
print(solution(12), 14200)