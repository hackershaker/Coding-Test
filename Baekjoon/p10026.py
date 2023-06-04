import sys


class Solution:
    def solution(self):
        n = int(sys.stdin.readline().strip())
        board = [sys.stdin.readline().strip() for _ in range(n)]
        count = {"R": 1, "G": 1, "B": 1}
        colormap = {2: "R", 3: "G", 5: "B", "R": 2, "G": 3, "B": 5}

        visited = set()
        normal = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i, j) not in visited:
                    stack = [(i, j)]
                    while stack:
                        node = stack.pop()
                        visited.add(node)
                        for x, y in (1, 0), (-1, 0), (0, 1), (0, -1):
                            r, c = node[0] + x, node[1] + y
                            if (
                                not (0 <= r < len(board) and 0 <= c < len(board[0]))
                                or (r, c) in visited
                            ):
                                continue
                            if board[r][c] == board[node[0]][node[1]]:
                                stack.append((r, c))
                    normal += 1

        weakness = 0
        visited = set()
        RGset = {"R", "G"}
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i, j) not in visited:
                    stack = [(i, j)]
                    while stack:
                        node = stack.pop()
                        visited.add(node)
                        for x, y in (1, 0), (-1, 0), (0, 1), (0, -1):
                            r, c = node[0] + x, node[1] + y
                            if (
                                not (0 <= r < len(board) and 0 <= c < len(board[0]))
                                or (r, c) in visited
                            ):
                                continue
                            if (
                                board[node[0]][node[1]] in RGset
                                and board[r][c] in RGset
                            ) or (
                                board[node[0]][node[1]] == "B" and board[r][c] == "B"
                            ):
                                stack.append((r, c))
                    weakness += 1

        print(str(normal) + " " + str(weakness))


if __name__ == "__main__":
    s = Solution()
    s.solution()
