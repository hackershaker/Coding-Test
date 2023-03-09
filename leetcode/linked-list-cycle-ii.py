# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        while head.next:
            if head.val > 10**5:
                head.val -= 2 * 10**5 + 1
                return head
            head.val += 2 * 10**5 + 1
            head = head.next
        return None
