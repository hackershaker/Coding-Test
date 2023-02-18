# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]
        while stack:
            node = stack.pop()
            if not node: continue
            self.swap(node)
            stack.extend([node.left, node.right])
        return root

    def swap(self, node):
        temp = node.left
        node.left = node.right
        node.right = temp

