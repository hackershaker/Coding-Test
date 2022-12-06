# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        evenNodes, oddNodes, oddStart, evenStart = None, None, None, None
        i = 1
        
        if not head: return head

        while head:
            temp = head.next
            if i % 2:
                if not oddNodes:
                    oddNodes = head
                    oddStart = head
                else:
                    oddNodes.next = head
                    oddNodes = oddNodes.next
                oddNodes.next = None
            
            else:
                if not evenNodes:
                    evenNodes = head
                    evenStart = head
                else:
                    evenNodes.next = head
                    evenNodes = evenNodes.next
                evenNodes.next = None
            head = temp
            i += 1

        oddNodes.next = evenStart
        return oddStart
