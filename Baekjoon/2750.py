if __name__=="__main__":
    n = int(input())
    l = []
    for _ in range(n):
        l.append(int(input()))

    for i in sorted(l):
        print(i)