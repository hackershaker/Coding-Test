# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random


class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        array = []
        node = self.head
        idx = 0
        while node:
            if len(array) == 0:
                array.append(node.val)
                idx += 1
                node = node.next
                continue
            if random.randint(0, idx) == 0:
                array[0] = node.val
            idx += 1
            node = node.next
        return array[0]


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
