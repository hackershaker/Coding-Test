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

if __name__=="__main__":
    n = int(input())
    solution(n)