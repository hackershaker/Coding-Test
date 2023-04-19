# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        answer = 0
        dic = {}

        nodes = []
        stack = deque([root])
        while stack:
            node = stack.popleft()
            if not node:
                continue
            nodes.append(node)
            stack.append(node.left)
            stack.append(node.right)

        while nodes:
            node = nodes.pop()
            zigZagDict = {"left": 0, "right": 0}
            if node.left:
                zigZagDict["left"] = 1 + node.left.path["right"]
            if node.right:
                zigZagDict["right"] = 1 + node.right.path["left"]

            answer = max(answer, max(zigZagDict.values()))
            node.path = zigZagDict

        return answer
