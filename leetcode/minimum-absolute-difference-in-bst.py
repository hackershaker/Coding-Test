# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        arr = []
        stack = [root]
        while stack:
            node = stack.pop()
            arr.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        arr.sort()
        answer = min([abs(arr[i] - arr[i + 1]) for i in range(len(arr) - 1)])
        return answer
