# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heappop, heappush


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dic = {i: lists[i] for i in range(len(lists))}
        heap = []
        for key in dic:
            if not dic[key]:
                continue
            heappush(heap, (dic[key].val, key))

        answer = ListNode(None, None)
        node = answer
        while heap:
            value, index = heappop(heap)
            element = dic[index]
            dic[index] = dic[index].next
            element.next = None

            node.next = element
            node = node.next

            if dic[index]:
                heappush(heap, (dic[index].val, index))

        return answer.next
