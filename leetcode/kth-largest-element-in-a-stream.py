from heapq import heappop, heappush
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        nums.sort()
        self.maxHeap = []
        while len(self.maxHeap) < k and nums:
            heappush(self.maxHeap, nums.pop())

    def add(self, val: int) -> int:
        heappush(self.maxHeap, val)
        while len(self.maxHeap) > self.k:
            heappop(self.maxHeap)
        return self.maxHeap[0]
