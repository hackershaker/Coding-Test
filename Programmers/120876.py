def solution(lines):
    def rever(li):
        return li if li[0] < li[1] else [li[1], li[0]]
    def getdupline(a,b):
        left = max(a[0],b[0])
        right = min(a[1],b[1])
        if left < right:
            return [left, right]
        else: 
            return

    def caldupline(l):
        total = 0
        l.sort(key=lambda x: x[0])
        for line in l: total += line[1]-line[0]
        for i in range(len(l)-1):
            temp = getdupline(l[i], l[i+1])
            if temp:
                total -= (temp[1]-temp[0])
        return total
    for i in range(len(lines)): lines[i] = rever(lines[i])
    order = [(0,1), (0,2), (1,2)]
    dupline = []
    for o in order:
        result = getdupline(lines[o[0]], lines[o[1]])
        if result: dupline.append(result)
    return caldupline(dupline)
        

print(solution([[0, 1], [2, 5], [3, 9]]), 2)
print(solution([[1, -1], [1, 3], [9, 3]]), 0)
print(solution([[0, 5], [3, 9], [1, 10]]), 8)
print(solution([[-1, 2], [3, 5], [7, 10]]), 0)
print(solution([[-1, 4], [3, 5], [7, 10]]), 1)
print(solution([[-1, 4], [3, 5], [7, 10]]), 1)
print(solution([[-1, 10], [3, 9], [5, 7]]), 6)
print(solution([[-1, 10], [3, 9], [8, 15]]), 7)
print(solution([[1,2], [2,3], [3,4]]), 0)
print(solution([[1,5], [2,3], [3,4]]), 2)
print(solution([[1,5], [1,3], [3,5]]), 4)
print(solution([[1,5], [1,5], [1,5]]), 4)
print(solution([[1,5], [2,5], [3,5]]), 3)
print(solution([[1,5], [1,5], [3,4]]), 4)
print(solution([[1,5], [1,5], [3,4]]), 4)
print(solution([[-2,5], [1,5], [0,6]]), 5)