def solution(k):
    list = [0,1]

    isEven = False
    while len(list) != k:
        i = len(list)+1
        temp = []
        if i%3 == 0: 
            temp.append(list[int(i/3)-1])
        if isEven: 
            temp.append(list[int(i/2)-1])
        temp.append(list[-1])
        list.append(1 + min(temp))
        isEven = not isEven
    print(list[k-1])
    return list[k-1]

def sol(k, numlist):
    if numlist[k-1] or k == 1:
        return numlist[k-1]
    temp = []
    r3, r2 = k%3, k%2
    if r3==0:
        temp.append(sol(int(k/3), numlist))
    if r2==0:
        temp.append(sol(int(k/2), numlist))
    if r2 != 0 or r3 != 0:
        temp.append(sol(k-1, numlist))

    numlist[k-1] = min(temp)+1
    return numlist[k-1]

if __name__=="__main__":
    n = int(input())
    numlist = [0,1] + [0] * (10**6-2)
    answer = sol(n, numlist=numlist)
    print(answer)