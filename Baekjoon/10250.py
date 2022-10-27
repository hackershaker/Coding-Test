def solution(h, w, n):
    xx = ((n-1) // h) + 1
    yy = (n-1) % h
    print(xx, yy)
    print(int(str(yy).rjust(2-len(str(yy)), '0') + str(xx).rjust(2-len(str(xx)), '0')))
    return int(str(yy).rjust(2-len(str(yy)), '0') + str(xx).rjust(2-len(str(xx)), '0'))


if __name__=="__main__":
    T = int(input())

    for _ in range(T):
        h, w, n = map(int, input().split(" "))
        solution(h, w, n)

