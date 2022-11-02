if __name__=="__main__":
    fibonacci = [[1,0],[0,1]]

    T = int(input())
    for _ in range(T):
        k = int(input())
        if len(fibonacci) >= k+1:
            print(" ".join(map(str, fibonacci[k])))
        else:
            while len(fibonacci) < k+1:
                fibonacci.append([x+y for x, y in zip(fibonacci[-1], fibonacci[-2])])
            print(" ".join(map(str, fibonacci[k])))