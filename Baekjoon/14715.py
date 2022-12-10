def solution():
    n = int(input())
    i = 2; treenode = 0
    while n > 1:
        m, r = divmod(n, i)
        if r == 0:
            treenode += 1
            n = m
        else:
            i += 1

    dic = getRow(treenode)
    return sorted(dic.items(), key=lambda x: (-x[1], -x[0]))[0][0]
    
def getRow(k):
    row = 0
    i = 1
    while True:
        row = 2**(i-1)
        if k < row:
            return {i-1:k, i-2: 2**(i-2)-(i//2)}
        if k == row:
            return {i-1:row}
        i += 1
        


if __name__=="__main__":
    answer = solution()
    print(answer)