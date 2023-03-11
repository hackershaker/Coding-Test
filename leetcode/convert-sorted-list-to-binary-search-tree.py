# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def __init__(self) -> None:
        self.array = []

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return
        while head:
            self.array.append(head.val)
            head = head.next

        return self.convertToHBBST(0, int(len(self.array) / 2), len(self.array) - 1)

    def convertToHBBST(self, start, headIdx, end):
        if start > end:
            return None
        return TreeNode(
            val=self.array[headIdx],
            left=self.convertToHBBST(
                start, int((start + headIdx - 1) / 2), headIdx - 1
            ),
            right=self.convertToHBBST(headIdx + 1, int((headIdx + 1 + end) / 2), end),
        )
