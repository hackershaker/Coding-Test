from heapq import heappop, heappush


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heappush(heap, -stone)
        while len(heap) > 1:
            y = -heappop(heap)
            x = -heappop(heap)
            if y > x:
                heappush(heap, -(y - x))

        return -heap[0] if heap else 0
