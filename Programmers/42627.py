from heapq import heappush, heappop
from collections import deque

def solution(jobs):
    jobs.sort(key=lambda x: x[0])
    jobschedule = deque([[0]])
    heap = []
    
    while jobschedule:
        sch = jobschedule.popleft()
        if len(sch) == len(jobs):
            # print(f"calculate {sch}")
            totaltime = 0; endtime = jobs[sch[0]][0]
            for jobidx in sch:
                totaltime += endtime - jobs[jobidx][0] + jobs[jobidx][1]
                endtime += jobs[jobidx][1]
            heappush(heap, totaltime)
        for i in range(len(jobs)):
            if i in sch: continue
            if jobs[sch[0]][0] <= jobs[i][0] <= jobs[sch[-1]][0] + jobs[sch[-1]][1]:
                jobschedule.append(sch + [i])
    
    return(int(heap[0]/len(jobs)))
    

print(solution(	[[0, 3], [1, 9], [2, 6]] ), 9)
print(solution(	[[0, 4], [1, 9], [2, 6], [3, 7]]*100 ), 9)