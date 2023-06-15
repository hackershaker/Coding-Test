# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        answer = 0
        level = 1
        curMaxSum = -float("inf")
        stack = [root]
        newStack = []
        s = 0
        while stack:
            node = stack.pop()
            s += node.val
            if node.left:
                newStack.append(node.left)
            if node.right:
                newStack.append(node.right)

            if not stack:
                if curMaxSum < s:
                    answer = level
                    curMaxSum = s
                s = 0
                level += 1
                stack = newStack
                newStack = []
        return answer
