# bfs 이용
# directed graph이기 때문에 바로 연결된 노드를 path에 붙임
# 끝 노드가 n-1인 path들을 모아서 answer에 저장

from collections import deque


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        answer = []
        stack = deque([[0]])
        while stack:
            path = stack.popleft()
            lastnode = path[-1]

            if lastnode == len(graph)-1:
                answer.append(path)
                continue

            for node in graph[lastnode]:
                stack.append(path + [node])

        return answer