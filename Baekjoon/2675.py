if __name__=="__main__":
    for _ in range(int(input())):
        n, string = input().split(" ")
        print("".join( [string[i]*int(n) for i in range(len(string))] ))