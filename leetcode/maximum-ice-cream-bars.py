# costs에서 최솟값인 아이스크림부터 사는 게 유리하다
# 따라서 최소 힙을 이용해 최솟값을 pop하고 
# coins를 넘지 않는 선에서 아이스크림을 구매


from heapq import heappush, heappop


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        heap = []

        for cost in costs:
            heappush(heap, cost)

        answer = 0

        while heap:
            if coins < heap[0]:
                break
            else:
                icecream = heappop(heap)
                coins -= icecream
                answer += 1

        return answer