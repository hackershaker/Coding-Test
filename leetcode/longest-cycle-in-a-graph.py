from typing import List


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        answer = -1
        visited = set()
        for i in range(len(edges)):
            if i in visited:
                continue
            path = {}
            index = 1
            stack = [i]
            checkNodes = set()
            while stack:
                node = stack.pop()
                if node in visited:
                    break
                checkNodes.add(node)
                if edges[node] == -1:
                    break
                if node in path:
                    answer = max(answer, index - path[node])
                    break
                path[node] = index
                index += 1
                nextnode = edges[node]
                stack.append(nextnode)
            visited.update(checkNodes)

        return answer
