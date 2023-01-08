# Dynamic Programming 이용
# 마지막 원소 0개, 1개, 2개를 포함하는 경우 중 가장 큰 값으로 저장


def solution():
    n = int(input())
    wine = [int(input()) for _ in range(n)]
    dic = {}

    for i in range(n+1):
        if i == 0: dic[i] = 0
        elif i == 1: dic[i] = wine[0]
        elif i == 2: dic[i] = wine[0]+wine[1]
        elif i == 3: dic[i] = max(wine[1]+wine[2], wine[0]+wine[2], dic[2])
        else: dic[i] = max(dic[i-1], wine[i-1] + dic[i-2], wine[i-1]+wine[i-2]+dic[i-3])

    return dic[n]

if __name__=="__main__":
    answer = solution()
    print(answer)