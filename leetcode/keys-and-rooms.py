
# union-find의 개념을 사용
# 0을 root node라고 생각
# 0부터 출발해 연결된 node의 parent를 0으로 치환
# 만약 모든 노드의 parent가 0이면 true
# 아니라면 False


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        nodes = [i for i in range(len(rooms))]

        stack = [0]
        while stack:
            node = stack.pop()
            for room in rooms[node]:
                if nodes[room] == 0: continue
                stack.append(room)
                nodes[room] = nodes[node]
        
        return len(set(nodes)) == 1