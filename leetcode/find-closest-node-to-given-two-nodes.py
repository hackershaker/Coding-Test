# node1, node2로부터 갈 수 있는 다른 노드들의 거리를 계산
# 공통적으로 갈 수 있는 노드들을 구한 후 두 거리의 최댓값 중 최솟값 반환
# 없으면 -1 반환


class Solution:
    def __init__(self) -> None:
        self.answer = -1
        self.distance = float("inf")

    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        distanceFromNode1 = self.findDistance(node1, edges)
        distanceFromNode2 = self.findDistance(node2, edges)

        for key in distanceFromNode1:
            if key in distanceFromNode2:
                maximumDistance = max(distanceFromNode1[key], distanceFromNode2[key])
                if maximumDistance < self.distance:
                    self.answer = key
                elif maximumDistance == self.distance:
                    self.answer = min(self.answer, key)
                else:
                    continue
        
        return self.answer

    def findDistance(self, start, edges):
        node = start; answer = {start:0}; visited = set()
        while True:
            nextnode = edges[node]
            if nextnode == -1:
                return answer
            else:
                if nextnode in visited:
                    answer[nextnode] = min(answer[nextnode], answer[node]+1)
                    return answer
                answer[nextnode] = answer[node] + 1
            visited.add(node)
            node = nextnode