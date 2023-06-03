from collections import defaultdict, deque


class Solution:
    def numOfMinutes(
        self, n: int, headID: int, manager: List[int], informTime: List[int]
    ) -> int:
        dic = defaultdict(list)
        for i in range(n):
            dic[manager[i]].append(i)

        answer = informTime[headID]
        stack = deque([(headID, 0)])
        while stack:
            node, t = stack.popleft()
            if informTime[node] == 0:
                answer = max(answer, t)
                continue
            for nextnode in dic[node]:
                stack.append((nextnode, t + informTime[node]))

        return answer
