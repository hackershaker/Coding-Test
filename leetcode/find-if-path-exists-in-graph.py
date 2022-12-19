# bfs 이용
# visited 리스트에 방문한 노드는 1, 방문하지 않은 노드는 0으로 저장
# bfs를 진행하여 destination 노드가 있다면 True 리턴
# stack이 다 소진될 때까지 destination 노드가 없다면 False 리턴
from collections import defaultdict, deque


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        dic = defaultdict(set)
        visited = [0] * n
        for edge in edges:
            dic[edge[0]].add(edge[1])
            dic[edge[1]].add(edge[0])
            
        stack = deque([source])
        visited[source] = 1
        while stack:
            node = stack.popleft()
            if node == destination: return True

            for vertex in dic[node]:
                if visited[vertex] == 0:
                    stack.append(vertex)
                    visited[vertex] = 1
            
        return False