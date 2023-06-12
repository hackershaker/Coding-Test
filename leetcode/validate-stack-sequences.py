from collections import deque
from typing import Deque, List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        popped: Deque[int] = deque(popped)
        stack = []
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[0]:
                stack.pop()
                popped.popleft()

        while stack:
            if stack[-1] == popped[0]:
                stack.pop()
                popped.popleft()
            else:
                return False
        return True
