# 빈 공간이 적은 곳부터 돌을 채워넣는 것이 유리
# 따라서 iterration을 돌면서 빈 공간을 최소 heap에 저장
# 이후 heap에서 최소값을 pop해서 채워진 bag 추가


from heapq import heappush, heappop
class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        answer = 0
        heap = []
        for i in range(len(rocks)):
            leftSpace = capacity[i]-rocks[i]
            if leftSpace == 0: answer += 1
            else: heappush(heap, leftSpace)

        while heap:
            space = heappop(heap)
            if additionalRocks >= space:
                answer += 1
                additionalRocks -= space
            else:
                break
        
        return answer
