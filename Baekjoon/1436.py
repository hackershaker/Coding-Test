def solution():
    n = int(input())
    numlist = []
    i = 1
    while len(numlist) < n:
        if "666" in str(i): numlist.append(i)
        i += 1
    return numlist[n-1]

if __name__=="__main__":
    answer = solution()
    print(answer)