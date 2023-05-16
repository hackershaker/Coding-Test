# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        answer = head.next
        preNode = ListNode(0, head)
        a, b = head, head.next
        while a and b:
            a.next = b.next
            preNode.next = b
            b.next = a
            a, b, = (
                b,
                a,
            )

            try:
                preNode = preNode.next.next
                a = a.next.next
                b =b.next.next
            except:
                break
        return answer
