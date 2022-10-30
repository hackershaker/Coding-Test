from collections import defaultdict, deque


def solution(info, edges):
    answer = 1
    dic = defaultdict(list)
    for edge in edges:
        dic[str(edge[0])].append(edge[1])

    stack = [[[0], deque([x for x in dic["0"]])]] # path, reserved node
    while stack:
        print("stack: ", stack)
        path, nodes = stack.pop()
        print(path)
        if path.count(path[-1]) > 1: continue
        lamb = sum([info[i] for i in path])
        answer = max(answer, lamb)
        wolf = len(path) - lamb
        print(f"wolf: {wolf}, lamb: {lamb}")
        for node in dic[str(path[-1])]:
            if info[node] == 0 or (info[node] == 1 and wolf + 1 < lamb):
                print(node, "is valid path")
                newnodes = nodes.extend(dic[str(node)])
                if node in newnodes: newnodes.remove(node)
                stack.append([path+[node], newnodes])
            else:
                continue
        else:
            if len(nodes) == 0:
                continue
            else:
                i = 0
                while i < len(nodes):
                    nextnode = nodes.popleft()
                    if nextnode == 0 or (nextnode == 1 and lamb > wolf + 1):
                        stack.append([path+[nextnode], nodes])
                    else:
                        nodes.append(nextnode)
                        i += 1
    return answer

print(solution(	[0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1], [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]] ))