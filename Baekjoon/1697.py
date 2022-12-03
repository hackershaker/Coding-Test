from collections import deque
def solution():
    n,k = map(int, input().split(" "))

    if k <= n: return n-k
    
    dic = {n:0}
    for i in range(0, n):
        dic[i] = n-i

    for i in range(n+1, k+2):
        if i % 2 == 0:
            dic[i] = min(dic.get(i-1, 100001), dic.get(i+1, 100001), dic.get(int(i/2), 100001)) + 1
        else:
            dic[i] = min(dic.get(i-1, 100001), dic.get(i+1, 100001)) + 1
        dic[i-1] = min(dic.get(i-1, 100001), dic[i]+1)
        dic[i+1] = min(dic.get(i+1, 100001), dic[i]+1)
        dic[2*i] = min(dic.get(2*i, 100001), dic[i]+1)

    # print(sorted(dic.items()))
    return dic[k]


def returnMinValue(dest, dic):
    if dest % 2 == 0:
        return min(dic[dest-1], dic[dest+1], dic[dest//2]) + 1
    else:
        return min(dic[dest-1], dic[dest+1]) + 1


if __name__=="__main__":
    answer = solution()
    print(answer)
