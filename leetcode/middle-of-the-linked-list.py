# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        linkedlist = [head]
        while True:
            head = head.next
            if head == None: break
            if head:
                linkedlist.append(head)

        return linkedlist[int(len(linkedlist)/2)]