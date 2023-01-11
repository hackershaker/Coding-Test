# 직관)
# 1) 가장 적은 시간에 심사하는 카운터에 많이 있을수록 유리하다는 생각을 함.
# 2) 그리고 그 카운터에서 t분이 걸릴 때 다른 카운터에서 t분 이하로 사람을 우선 배치하는 것이 최적화.

# 따라서 가장 작은 심사 시간 카운터에 들어가는 사람 수를 이분탐색.
# 직관 2)처럼 t분보다 작게 각 카운터에 사람을 채워넣고
# 총 사람 수가 n명보다 작게 되도록 사람 설정.

# 그 후 heap을 이용하여 나머지 사람 채움.




from heapq import heappop, heappush


def solution(n, times):
    times.sort()

    baseUnitFloor, baseUnitCeil = 1, n
    while baseUnitFloor < baseUnitCeil:
        mid = int((baseUnitFloor+baseUnitCeil) / 2)
        # print("start:", baseUnitFloor,"mid:", mid, "end:", baseUnitCeil)

        minTimeTotal = times[0] * mid
        needPersonNum = mid

        for i in range(1, len(times)):
            m = minTimeTotal // times[i]
            needPersonNum += m
        # print("최적화에 필요한 사람: ", needPersonNum)

        if needPersonNum > n: 
            baseUnitCeil = mid-1
        elif needPersonNum == n:
            break
        else: baseUnitFloor = mid+1

    baseUnitFloor -= 1
    heap = []; answer = 0; baseTime = times[0] * baseUnitFloor; people = 0
    for i in range(len(times)):
        heappush(heap, ((baseTime//times[i]) * times[i] + times[i], times[i]))
        people += baseTime//times[i]

    while people < n:
        time, taskTime = heappop(heap)
        answer = max(answer, time)
        heappush(heap, (time+taskTime, taskTime))
        people += 1
    
    return answer