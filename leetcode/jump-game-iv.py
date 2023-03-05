from collections import defaultdict, deque
from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        dic = defaultdict(set)
        # key: integer, value: indexs set whose arr value is integer
        for index in range(len(arr)):
            dic[arr[index]].add(index)

        # minimum step save in distanceArray
        distanceArray = [-1 for _ in range(len(arr))]
        distanceArray[0] = 0
        stack = deque([0])
        visitedNode = {0}
        while stack:
            idx = stack.popleft()
            # if index is last index, return
            if idx == len(arr) - 1:
                return distanceArray[-1]
            # explore same value indexes
            for i in dic[arr[idx]]:
                if i != idx:
                    if distanceArray[i] not in visitedNode:
                        distanceArray[i] = distanceArray[idx] + 1
                        stack.append(i)
                        visitedNode.add(i)
            # after explore, there is no need to save
            # because we traverse all indexes of arr[idx]
            # so clear arr[idx]
            dic[arr[idx]] = set()
            # explore front node and end node of idx
            if idx + 1 < len(arr):
                if idx + 1 not in visitedNode:
                    distanceArray[idx + 1] = distanceArray[idx] + 1
                    stack.append(idx + 1)
                    visitedNode.add(idx + 1)
            if idx - 1 >= 0:
                if idx - 1 not in visitedNode:
                    distanceArray[idx - 1] = distanceArray[idx] + 1
                    stack.append(idx - 1)
                    visitedNode.add(idx - 1)
