# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        tree1, tree2 = self.getLeafNodes(root1), self.getLeafNodes(root2)
        return tree1 == tree2

    def getLeafNodes(self, tree) -> list:
        if tree == None: return []
        if not tree.left and not tree.right:
            return [tree.val]
        return self.getLeafNodes(tree.left) + self.getLeafNodes(tree.right)