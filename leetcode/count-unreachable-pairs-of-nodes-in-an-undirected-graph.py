from collections import defaultdict


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        edgeDict = defaultdict(list)
        for edge in edges:
            edgeDict[edge[0]].append(edge[1])
            edgeDict[edge[1]].append(edge[0])

        network = []
        visited = set()
        for i in range(n):
            if i not in visited:
                graph = 0
                stack = [i]
                while stack:
                    node = stack.pop()
                    if node in visited:
                        continue
                    visited.add(node)
                    graph += 1

                    for nextnode in edgeDict[node]:
                        stack.append(nextnode)
                network.append(graph)

        total = sum(network) ** 2
        answer = int((total - sum(map(lambda x: x**2, network))) / 2)

        return answer
