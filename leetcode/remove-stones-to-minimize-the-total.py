# 남은 돌의 수가 최소가 되려면 많이 쌓여있는 돌부터 제거하는 게 유리
# 따라서 heap에 돌들의 갯수를 넣고 최댓값을 빼내서 piles 갱신
# k만큼 operation 후 piles의 합 return

from heapq import heappop, heappush
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []
        for i in range(len(piles)):
            heappush(heap, (-piles[i], i))

        for _ in range(k):
            height, index = heappop(heap)
            piles[index] -= int(-height/2)
            heappush(heap, (-piles[index], index))

        return sum(piles)