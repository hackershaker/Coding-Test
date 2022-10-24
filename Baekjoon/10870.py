if __name__=="__main__":
    n = int(input())
    fibbo = [0, 1]
    while len(fibbo) < n+1:
        fibbo.append(fibbo[-1] + fibbo[-2])
    print(fibbo[n])