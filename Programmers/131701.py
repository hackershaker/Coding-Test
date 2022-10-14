def solution(elements):
    windowsize = len(elements)
    elements.extend(elements)
    sumlist = [[i, i, elements[i]] for i in range(len(elements))]
    sumset = set(elements)
    print(sumlist)
    answer = 0
    
    while True:
        temp = []
        for l in sumlist:
            if l[1] + 1 >= len(elements): break
            temp.append([l[0], l[1]+1, l[2]+elements[l[1]+1]])
            sumset.add(l[2]+elements[l[1]+1])
        sumlist = temp
        if sumlist[0][1] - sumlist[0][0] + 1 == windowsize: break
    return len(sumset)

print(solution([7,9,1,1,4]))