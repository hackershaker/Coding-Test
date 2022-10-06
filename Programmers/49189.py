def solution(n, edge):
    answer = 0
    graph = {str(x): [] for x in range(1,n+1)}
    for nodes in edge:
        graph[str(nodes[0])] += [nodes[1]]
        graph[str(nodes[1])] += [nodes[0]]
    print(graph)
    return answer



print(solution(	6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))