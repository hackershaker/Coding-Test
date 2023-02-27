"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


from typing import List


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def __init__(self) -> None:
        self.grid = None

    def construct(self, grid: List[List[int]]) -> "Node":
        n = len(grid)
        self.grid = grid
        gridSumArray = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

        for i in range(1, len(gridSumArray)):
            for j in range(1, len(gridSumArray)):
                gridSumArray[i][j] = (
                    gridSumArray[i - 1][j]
                    + gridSumArray[i][j - 1]
                    - gridSumArray[i - 1][j - 1]
                    + grid[i - 1][j - 1]
                )

        return self.quadTree(gridSumArray, 0, n - 1, 0, n - 1)

    def quadTree(self, prefixSum, startRow, endRow, startColumn, endColumn) -> "Node":
        totalSum = (
            prefixSum[endRow + 1][endColumn + 1]
            - prefixSum[startRow][endColumn + 1]
            - prefixSum[endRow + 1][startColumn]
            + prefixSum[startRow][startColumn]
        )
        if startRow == endRow:
            return Node(
                True if self.grid[startRow][startColumn] else False,
                True,
                None,
                None,
                None,
                None,
            )
        elif totalSum == (endRow - startRow + 1) ** 2:
            return Node(True, True, None, None, None, None)
        elif totalSum == 0:
            return Node(False, True, None, None, None, None)
        else:
            width = int((endRow - startRow + 1) / 2)
            topLeftNode = self.quadTree(
                prefixSum,
                startRow,
                startRow + width - 1,
                startColumn,
                startColumn + width - 1,
            )
            topRightNode = self.quadTree(
                prefixSum,
                startRow,
                startRow + width - 1,
                startColumn + width,
                endColumn,
            )
            bottomLeftNode = self.quadTree(
                prefixSum,
                startRow + width,
                endRow,
                startColumn,
                startColumn + width - 1,
            )
            bottomRightNode = self.quadTree(
                prefixSum, startRow + width, endRow, startColumn + width, endColumn
            )

            return Node(
                True, False, topLeftNode, topRightNode, bottomLeftNode, bottomRightNode
            )
