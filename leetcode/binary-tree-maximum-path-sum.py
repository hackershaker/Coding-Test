# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
class Solution:
    def __init__(self) -> None:
        self.maxValue = -float("inf")
        
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        total = self.getSum(root, 0)
        return max(self.maxValue, total)

    def getSum(self, root, parent = 1):
        if not root: return 0
        leftMax, rightMax = self.getSum(root.left), self.getSum(root.right)
        self.maxValue = max(self.maxValue, root.val + leftMax + rightMax, root.val+leftMax, root.val+rightMax, root.val)
        if parent:
            return max(root.val, root.val+leftMax, root.val+rightMax)
        else:
            leftMax, rightMax = self.getSum(root.left), self.getSum(root.right)
            return max(root.val, root.val+leftMax, root.val+rightMax, root.val+leftMax+rightMax)