# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        answer = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if not node: continue

            answer = max(answer, self.getValue(node))
            stack.extend([node.left, node.right])
        
        return answer


    def getValue(self, root: Optional[TreeNode]) -> int:
        value = []; rootNode = root.val
        stack = [root.left, root.right]
        while stack:
            node = stack.pop()
            if not node: continue
            value.append(abs(rootNode - node.val))
            stack.extend([node.left, node.right])

        return max(value) if len(value)>0 else 0

