import sys
if __name__=="__main__":
    l = []
    n = int(input())
    for _ in range(n):
        i = int(sys.stdin.readline().strip())
        l.append(i)

    l.sort()
    for i in range(len(l)): print(l[i])