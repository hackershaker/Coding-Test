def isOne(k):
    if k < 10:
        return True
    else:
        k = str(k)
        r = int(k[1]) - int(k[0])

        for i in range(1, len(k)):
            if int(k[i]) - int(k[i-1]) != r:
                return False
        return True

def solution(k):
    answer = 0
    for i in range(1,k+1):
        if isOne(i):
            answer += 1
    print(answer)

if __name__=="__main__":
    n = int(input())
    solution(n)
    