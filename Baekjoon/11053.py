def solution():
    n = int(input())
    numlist = list(map(int, input().split(" ")))
    LISList = []

    for i in range(n):
        LISList.append([numlist[i], 1])
        for k in range(len(LISList)-1):
            if LISList[k][0] < LISList[i][0]:
                LISList[i][1] = max(LISList[i][1], LISList[k][1]+1)
    
    return max(LISList, key=lambda x: x[1])[1]



if __name__=="__main__":
    answer = solution()
    print(answer)