if __name__=="__main__":
    m, n = map(int, input().split(" "))
    l = [x for x in range(1,n+1)]
    l[0] = 0

    for i in range(2, int(n/2)+1):
        k = 2
        while k*i-1 < len(l):
            l[k*i-1] = 0
            k += 1

    for j in range(m, n+1):
        if l[j-1]:
            print(l[j-1])