from collections import defaultdict
def solution():
    n = int(input())
    network = defaultdict(list)
    for _ in range(int(input())):
        a, b = input().split(" ")
        network[a].append(b)
        network[b].append(a)

    stack = ["1"]
    computerSet = set()
    while stack:
        node = stack.pop()
        for com in network[node]:
            if com not in computerSet:
                computerSet.add(com)
                stack.append(com)

    return len(computerSet - {"1"})

if __name__=="__main__":
    answer = solution()
    print(answer)