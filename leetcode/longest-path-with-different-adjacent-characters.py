# 클래스 변수 self.answer에 모든 경로의 최댓값 갱신
# longestpathfromparent가 자식 노드로부터 연결되는 path 중 최댓값을 반환
# 최대 2개까지 root노드에 붙여서 path를 만들 수 있음. 이 값이 bothPath



from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def __init__(self) -> None:
        self.answer = 0

    def longestPath(self, parent: List[int], s: str) -> int:
        dic = defaultdict(list)
        for i in range(1, len(parent)):
            dic[parent[i]].append(i)

        self.longestPathfromParent(0, dic, s)
        return self.answer

    def longestPathfromParent(self, root: int, dic: dict, s: str) -> int:
        bothPath, sidePath = 1,1
        heap = []
        for child in dic[root]:
            temp = self.longestPathfromParent(child, dic, s)
            if s[root] != s[child]:
                heappush(heap, -temp)
                sidePath = max(sidePath, temp+1)

        i = 0
        while i < 2:
            try:
                bothPath -= heappop(heap)
                i += 1
            except:
                break

        print(f"From root {root}, most longest path is {sidePath} and bothpath is {bothPath}")
        self.answer = max(self.answer, bothPath)
        return sidePath