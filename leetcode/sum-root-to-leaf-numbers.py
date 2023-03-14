# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        answer = 0
        stack = [(0, root)]
        while stack:
            value, node = stack.pop()
            print(value, node)
            if node.left == None and not node.right == None:
                answer += value * 10 + node.val
                continue
            if node.left:
                stack.append((value * 10 + node.val, node.left))
            if node.right:
                stack.append((value * 10 + node.val, node.right))
        return int(answer / 2)
