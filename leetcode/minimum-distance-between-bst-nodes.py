# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self) -> None:
        self.distance = float("inf")

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        while stack:
            node = stack.pop()
            if not node: continue
            self.explore(node)
            stack.extend([node.left, node.right])
        return self.distance

    def explore(self, root):
        rootVal = root.val

        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                self.distance = min(self.distance, abs(rootVal-node.left.val))
                stack.append(node.left)
            if node.right:
                self.distance = min(self.distance, abs(rootVal-node.right.val))
                stack.append(node.right)