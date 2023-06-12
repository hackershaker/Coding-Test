from heapq import heappop, heappush, heappushpop


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        heap = []
        total = 0
        answer = 0
        coeff = 0
        for a, b in zip(nums1, nums2):
            heappush(heap, (-b, a))

        nums1Heap = []
        for _ in range(k):
            multiply, plus = heappop(heap)
            total += plus
            coeff = -multiply
            heappush(nums1Heap, plus)
        answer = max(answer, total * coeff)

        while heap:
            m, p = heappop(heap)
            if p > nums1Heap[0]:
                total += p
                total -= heappushpop(nums1Heap, p)
            answer = max(answer, total * -m)

        return answer
