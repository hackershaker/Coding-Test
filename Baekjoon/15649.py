from collections import deque
def solution():
    n,m = map(int, input().split(" "))

    stack = deque([[]])
    while stack:
        k = stack.popleft()

        if len(k) == m:
            print(" ".join(map(str, k)))
            continue
        
        for i in range(1, n+1):
            if i not in k:
                stack.append(k + [i])

if __name__=="__main__":
    solution()