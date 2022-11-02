def getScaleSum(sumlist, room, s):
    if s <= 0: return 0
    return sumlist[s-1].get(str(room), 0)

def solution(sumlist):
    dic = {}
    target = len(sumlist)+1
    for num in range(2, target+1):
        dic[str(num)] = 0
        if num == 2:
            if target > 6:
                continue
            else:
                temp = 0
                for i in range(1, 4):
                    if 0 < target-i < 4: temp += 1
                dic["2"] = temp
            continue
        for i in range(1,4):
            dic[str(num)] += getScaleSum(sumlist, num-1, target-i)
    sumlist.append(dic)
    return sumlist

def solution2(n):
    answer = set()
    stack = [([1], 1),([2], 2),([3], 3)]

    while stack:
        numbers, total = stack.pop()
        if total > n:
            continue
        if total == n:
            answer.add(tuple(numbers))
            continue

        for i in range(1,4):
            if total + i < n:
                stack.append(( numbers+[i], total+i ))
            elif total + i == n:
                answer.add(tuple(numbers+[i]))
            else:
                continue

    return len(answer)

if __name__=="__main__":
    sumlist = [{"1":1}, {"2":1}]

    T = int(input())
    # solution 1
    # for _ in range(T):
    #     n = int(input())
    #     if len(sumlist) >= n:
    #         print(sum(sumlist[n-1].values()))
    #     else:
    #         while len(sumlist) < n:
    #             sumlist = solution(sumlist)
    #         print(sum(sumlist[n-1].values()))

    #solution 2
    for _ in range(T):
        print(solution2(int(input())))

def testcode(k):
    return solution2(k)


