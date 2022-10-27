if __name__=="__main__":
    n = int(input())

    for i in reversed(range(1, n+1)):
        print(('*'*i).rjust(n, " "))
