from collections import deque, defaultdict

def dfs(v, dic):
    stack = [v]; visited = []
    while stack:
        path = stack.pop()
        if path not in visited:
            visited.append(path)
        temp = []
        for node in dic[str(path)]:
            if node not in visited: 
                temp = [node] + temp
        stack.extend(temp)
    
    print(" ".join(map(str, visited)))
    return visited
                
def bfs(v, dic):
    visited = []
    stack = deque([v])
    while stack:
        path = stack.popleft()
        if path not in visited:
            visited.append(path)
        for node in dic[str(path)]:
            if node not in visited:
                stack.append(node)
        
    print(" ".join(map(str, visited)))
    return visited

def solution(n, m, v, lines):
    dic = defaultdict(list)
    temp = []
    for line in lines:
        temp.append(line)
        temp.append(list(reversed(line)))
    temp.sort(key=lambda x : (x[0], x[1]))
    for points in temp:
        dic[str(points[0])].append(points[1])
    
    return dfs(v, dic), bfs(v, dic)

import sys
if __name__=="__main__":
    n, m, v = map(int, input().split())
    temp = []
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().strip().split(" "))
        temp.append([a,b])
    
    solution(n,m,v,temp)