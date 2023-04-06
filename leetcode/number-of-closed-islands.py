from collections import deque


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        answer = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ord = (i, j)

                if grid[i][j] == 0:
                    if ord in visited:
                        continue
                    stack = deque([ord])
                    isEdgeAdjcent = False
                    while stack:
                        coord = stack.popleft()
                        if not (
                            0 <= coord[0] < len(grid) and 0 <= coord[1] < len(grid[0])
                        ):
                            isEdgeAdjcent = True
                            continue
                        if grid[coord[0]][coord[1]] == 1:
                            continue
                        else:
                            if coord not in visited:
                                visited.add(coord)
                            else:
                                continue

                        u, d, r, l = (-1, 0), (1, 0), (0, 1), (0, -1)
                        for next in u, d, r, l:
                            nextord = (coord[0] + next[0], coord[1] + next[1])
                            stack.append(nextord)

                    if isEdgeAdjcent:
                        continue
                    if len(stack) == 0:
                        answer += 1

        return answer
