# bfs이용
# 리스트에 각 노드까지 갈 수 있는 최소 거리 갱신



from collections import defaultdict, deque
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dic = defaultdict(list)
        for a,b,cost in flights:
            dic[a].append((b, cost))

        costsList = [-1]*n
        stack = deque([(src, 0, 0),]) #current node, # of stops, cost
        while stack:
            node, distance, totalCost = stack.popleft()
            
            if node != dst:
                if distance-1 > k or (costsList[node] != -1 and totalCost >= costsList[node]):
                    continue
                else:
                    costsList[node] = totalCost if costsList[node] == -1 else min(costsList[node], totalCost)
            else:
                if distance-1 <= k:
                    costsList[node] = totalCost if costsList[node] == -1 else min(costsList[dst], totalCost)
                continue

            for nextnode, cost in dic[node]:
                stack.append((nextnode, distance+1, totalCost+cost))

        return costsList[dst]