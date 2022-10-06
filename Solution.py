def solution(numbers):
    answer = []
    n = 0
    def dfs(tree):
        stack = [int(len(tree)/2) + 1]
        while stack:
            parentnode = stack.pop()
            leftnode = parentnode - int(parentnode / 2)
            rightnode = parentnode + int(parentnode / 2)

            if parentnode != 1: return 0
            else:
                if leftnode <= len(tree): stack.append(leftnode)
                if rightnode <= len(tree): stack.append(leftnode)

        return 1

    for num in numbers:
        while True:
            if int(2**(n+1) - 1) >= num: break
            n += 1

        height = n
        num2 = bin(num).replace('0b', "")
        for i in range(2**height - len(num2) - 1):
            if len(num2) == 2**height -1:
                
            treenum = '0'*i + bin(num).replace('0b', "") + '0'*(2**height - len(num2) -1 - i )
            print(treenum)
            print(dfs(treenum))
    
    return answer


print(solution([7, 5, 9]))