from collections import deque, defaultdict

def dfs(v):
    stack = [[v]]
    while stack:
        path = stack.pop()
        if len(path) == n:
            print(" ".join(path))
            return
        


def bfs(v):
    pass

import sys
if __name__=="__main__":
    n, m, v = map(int, input().split())
    dic = defaultdict(list)
    for _ in range(m):
        a, b = map(int, sys.stdin.readline.strip().split(" "))
        dic[str(a)].append(b)
        dic[str(b)].append(a)

    dfs(v)
    bfs(v)