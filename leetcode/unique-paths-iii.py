# bfs 이용
# path: 방문한 노드의 집합
# 마지막 노드에서 4방향으로 갈 수 있는지 조사
# path에 갈 노드가 이미 있다면 건너뜀
# walkable: grid값이 -1이 아닌, 즉 갈 수 있는 모든 길의 합
# path 값이 walkable이 되고 마지막 길의 grid의 값이 2일 때의 수를 return



from collections import deque


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        stack = deque([]); answer = 0
        walkable = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != -1: walkable += 1
                if grid[i][j] == 1:
                    stack.append([{(i,j)}, (i,j)])

        while stack:
            path, lastnode = stack.popleft()

            if grid[lastnode[0]][lastnode[1]] == 2:
                if len(path) == walkable:
                    print(path)
                    answer += 1
                continue

            u, d, r, l = (1,0), (-1,0), (0,1), (0,-1)

            for p in u,d,r,l:
                nextnode = (lastnode[0]+p[0], lastnode[1]+p[1])

                if nextnode not in path and (0 <= nextnode[0] < len(grid)) and (0 <= nextnode[1] < len(grid[0])) and grid[nextnode[0]][nextnode[1]] != -1:
                    stack.append([path | {nextnode}, nextnode])

        return answer