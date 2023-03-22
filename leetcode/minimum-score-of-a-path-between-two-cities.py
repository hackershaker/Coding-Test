from collections import defaultdict
from typing import List


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        roadDict = defaultdict(list)
        for road in roads:
            roadDict[road[0]].append([road[1], road[2]])
            roadDict[road[1]].append([road[0], road[2]])

        stack = [1]
        path = [float("inf") for _ in range(n + 1)]
        while stack:
            edge = stack.pop()
            for nextEdge, distance in roadDict[edge]:
                minRoad = min(path[edge], path[nextEdge], distance)
                if minRoad < path[nextEdge]:
                    path[nextEdge] = minRoad
                    stack.append(nextEdge)

        return path[n]
