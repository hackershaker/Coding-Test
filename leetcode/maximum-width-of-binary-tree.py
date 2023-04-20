# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        answer = 0
        stack = deque([(1, root)])
        minval, maxval = float("inf"), -float("inf")
        newstack = []
        while stack:
            idx, node = stack.popleft()
            minval = min(minval, idx)
            maxval = max(maxval, idx)
            if node.left:
                newstack.append((idx * 2, node.left))
            if node.right:
                newstack.append((idx * 2 + 1, node.right))

            if not stack:
                if not newstack:
                    answer = max(answer, maxval - minval)
                    break
                else:
                    answer = max(answer, maxval - minval)
                    stack = deque(newstack)
                    newstack = []
                    minval, maxval = float("inf"), -float("inf")
        return answer+1


