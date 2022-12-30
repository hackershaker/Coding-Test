# curtime : task가 실행 완료된 현재 시간
# availableTasks : curtime 시점에서 실행 가능한 task들의 최소 heap
# dic : enqueue 시간별로 task를 모아둔 dictionary

# 초기 설정: availableTasks에 가장 빨리 queue에 들어오는 task를 담고
# curtime 은 enqueue시간 + processing시간으로 설정
# 이후 enqueueTimeHeap의 최소 시간이 curtime보다 작거나 같으면
# availableTasks에 추가
# enqueueTimeHeap의 최소 시간이 curtime보다 크면 availableTasks에서
# 최소 processingTime인 task를 추출해 curtime 갱신

# enqueueTimeHeap이 빌 때까지 반복 후 availableTasks에 있는 task를 하나씩 빼면서 
# answer 갱신


from collections import defaultdict
from heapq import heappop, heappush, heapify
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        dic = defaultdict(list); curtime = 0; answer = []
        availableTasks = []

        for i in range(len(tasks)):
            dic[tasks[i][0]].append((tasks[i][1], i))

        enqueueTimeHeap = list(dic.keys())
        heapify(enqueueTimeHeap)

        curtime += enqueueTimeHeap[0]
        for task in dic[enqueueTimeHeap[0]]: heappush(availableTasks, task)
        heappop(enqueueTimeHeap)

        while enqueueTimeHeap:
            if not availableTasks:
                t = heappop(enqueueTimeHeap)
                for task in dic[t]: heappush(availableTasks, task)
                processingTime, index = heappop(availableTasks)
            else:
                t = enqueueTimeHeap[0]
                processingTime, index = heappop(availableTasks)

            curtime = t + processingTime if curtime < t else curtime + processingTime
            answer.append(index)
            while enqueueTimeHeap:
                if curtime >= enqueueTimeHeap[0]:
                    time = heappop(enqueueTimeHeap)
                    for task in dic[time]: heappush(availableTasks, task)
                else:
                    break

        while availableTasks:
            ptime, index = heappop(availableTasks)
            answer.append(index)
            curtime += ptime
            print(curtime, availableTasks)
            

        return answer