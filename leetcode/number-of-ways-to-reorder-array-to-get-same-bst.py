from math import factorial
from typing import List


class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        root = Node(val=nums[0])
        for i in range(1, len(nums)):
            temp = root
            while True:
                if nums[i] < temp.val:
                    if not temp.left:
                        temp.left = Node(val=nums[i])
                        break
                    else:
                        temp = temp.left
                else:
                    if not temp.right:
                        temp.right = Node(val=nums[i])
                        break
                    else:
                        temp = temp.right
        return (self.recur(root)[1] - 1) % (10**9 + 7)

    def recur(self, head):
        if not head:
            return (0, 1)
        lst_num, lst_order = self.recur(head.left)
        rst_num, rst_order = self.recur(head.right)
        # print(head.val, lst_num, lst_order, rst_num, rst_order)
        result = (
            lst_num + rst_num + 1,
            self.insertSequence(lst_num, rst_num) * lst_order * rst_order,
        )
        # print(head.val, result)
        return result

    def insertSequence(self, a, b):
        # a+b C b
        return factorial(a + b) // (factorial(b) * factorial(a))


class Node:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right
