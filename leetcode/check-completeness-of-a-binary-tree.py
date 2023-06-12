# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        nodeNumber = 0
        nodeSum = 0
        stack = deque([(1, root)])
        while stack:
            index, node = stack.popleft()
            nodeNumber += 1
            nodeSum += index
            if node.left:
                stack.append((index * 2, node.left))
            if node.right:
                stack.append((index * 2 + 1, node.right))
        return int((nodeNumber*(nodeNumber+1))/2) == nodeSum