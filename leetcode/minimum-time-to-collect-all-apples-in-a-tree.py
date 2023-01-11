# distance함수를 통해 재귀적으로 거리 계산
# 만약 자식 노드가 사과가 있거나 거리가 0이 아니면 이 자식노드로는 무조건 순회 돌아야 하므로
# 가는 거리와 오는 거리인 2를 더해준다.
# 모든 거리를 합산하여 return


from collections import defaultdict


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        dic = defaultdict(list); parents = set()
        for edge in edges:
            dic[edge[0]].append(edge[1])
            dic[edge[1]].append(edge[0])

        return self.distance(0, dic, hasApple, None)

    def distance(self, root: int, dic: dict, appleList: list, parent) -> int:
        if root not in dic.keys():
            return 0

        childNode = {node:self.distance(node, dic, appleList, root) for node in dic[root] if node != parent}
        answer = 0

        for child in childNode:
            if appleList[child] or childNode[child]: answer += 2

        return answer + sum(childNode.values())