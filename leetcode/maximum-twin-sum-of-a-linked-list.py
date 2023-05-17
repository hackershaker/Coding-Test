# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        i = 0
        while fast:
            slow, fast = slow.next, fast.next.next
            i += 1
        pre, post = head, slow
        arr = [0] * i
        for i in range(len(arr)):
            arr[i] += pre.val
            arr[len(arr) - i - 1] += post.val
            pre, post = pre.next, post.next
        return max(arr)