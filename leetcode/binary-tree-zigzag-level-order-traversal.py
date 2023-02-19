# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        stack = deque([root])
        isReverse = False
        while True:
            traverseRow = []
            newStack = deque([])
            while stack:
                node = stack.popleft()
                if node: 
                    traverseRow.append(node.val)
                    newStack.append(node.left)
                    newStack.append(node.right)
            stack = newStack
            if not traverseRow: break
            if isReverse:
                answer.append(traverseRow[::-1])
            else:
                answer.append(traverseRow)
            isReverse = not isReverse

        return answer