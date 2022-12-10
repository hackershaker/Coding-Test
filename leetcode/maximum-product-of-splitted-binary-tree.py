# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        sumlist = []
        total = self.getSum(root, sumlist)
        sumlist.sort(key=lambda x: abs(2*x-total))
        return sumlist[0]*(total - sumlist[0]) % (10**9 + 7)

    def getSum(self, root, array):
        if not root: return 0
        s = self.getSum(root.left, array) + root.val + self.getSum(root.right, array)
        array.append(s)
        return s