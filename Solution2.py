def solution(cap, n, deliveries, pickups):
    answer = -1
    distance = 0
    allbox = sum(deliveries) + sum(pickups)

    temp = 0

    k = 0
    while k < 20:

        bus = [0, 0]  # 배달, 수거
        maxb = 0
        for i in range(n):
            if deliveries[i] == 0:
                continue
            elif bus[0] + deliveries[i] <= cap:
                bus[0] += deliveries[i]
                temp += deliveries[i]
                deliveries[i] = 0
                maxb = max(maxb, i)
            else:
                deliveries[i] = deliveries[i] - (cap - bus[0])
                temp += cap - bus[0]
                break

        maxs = 0
        for i in reversed(range(n)):
            if pickups[i] == 0:
                continue
            elif bus[1] == cap:
                break
            elif bus[1] + pickups[i] <= cap:
                bus[1] += pickups[i]
                temp += pickups[i]
                pickups[i] = 0
                maxs = max(maxs, i)
            else:
                pickups[i] = pickups[i] - (cap - bus[1])
                temp += cap - bus[1]
                break
        k += 1
        distance += (max(maxb, maxs) + 1) * 2
        if temp == allbox:
            break

    answer = distance
    return answer
