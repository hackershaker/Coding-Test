if __name__=="__main__":
    A, B, C = map(int, input().split(" "))
    x = 0
    if B >= C: print(-1)
    else:
        x = int(A/(C-B))+1
        print(x)
        