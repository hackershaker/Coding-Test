def solution(h, w, n):
    xx = str(((n-1) // h) + 1)
    yy = str((n-1) % h + 1)

    xx = xx.zfill(2)
    yy = yy.zfill(2)
    print(int( yy+xx ))
    return int( yy+xx )


if __name__=="__main__":
    T = int(input())

    for _ in range(T):
        h, w, n = map(int, input().split(" "))
        solution(h, w, n)

