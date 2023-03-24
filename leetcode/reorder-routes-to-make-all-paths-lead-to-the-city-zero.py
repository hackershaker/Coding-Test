from collections import defaultdict
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        answer = 0
        dest, arr = defaultdict(list), defaultdict(list)
        for connection in connections:
            d, a = connection
            dest[d].append(a)
            arr[a].append(d)

        stack = [0]
        visited = set()
        while stack:
            node = stack.pop()
            visited.add(node)

            for d in dest[node]:
                if d not in visited:
                    answer += 1
                    stack.append(d)

            for a in arr[node]:
                if a not in visited:
                    stack.append(a)

        return answer
