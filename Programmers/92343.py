from collections import defaultdict, deque

def solution(info, edges):
    answer = 1
    dic = defaultdict(list)
    for edge in edges:
        dic[str(edge[0])].append(edge[1])

    stack = deque([[[0], []]])
    while stack:
        # print(stack)
        path, willvisit = stack.popleft()

        temp = [info[i] for i in path].count(0)
        lamb = temp if temp > len(path)-temp else 0
        if lamb == 0: continue
        answer = max(answer, lamb)

        willvisit.extend(dic[str(path[-1])])

        for node in willvisit:
            stack.append([path+[node], [x for x in willvisit if x != node and x not in path]])

    return answer

print(solution(	[0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1], [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]] ))
print(solution(	[0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0], [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]))