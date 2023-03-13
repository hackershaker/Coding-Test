# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isNodeSymmetric(root, root)

    def isNodeSymmetric(self, a, b):
        if a == None and b == None:
            return True
        if (a == None) ^ (b == None):
            return False
        if a.val != b.val:
            return False
        return self.isNodeSymmetric(a.left, b.right) and self.isNodeSymmetric(
            a.right, b.left
        )
