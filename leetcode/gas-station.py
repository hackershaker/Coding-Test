# gas와 cost의 길이가 10^5까지 될 수 있으므로 효율성 제고 필요.
# lastGas = gas와 cost의 차로 이루어진 list
# 일단 lastGas의 출발점이 0 이상이어야 하고
# 시계방향으로 더해나갔을 때의 합이 모두 0 이상이어야 한다.
# 그래서 이걸 어떻게 구할까 생각하다가
# 누적합을 구하고 lastGas가 rotate 되었을 때를 고려해보았다.
# 그래서 발견한 규칙은 rotate된 원소가 누적합 각각의 원소에서 빼지고
# 마지막 누적합의 원소는 변하지 않는다는 것이다(마지막 원소는 모든 원소의 합이므로).
# 즉 i번 rotate한다면 누적합 (i-1)번 원소가 누적합에 모두 빼지고 마지막 원소는 그대로 된 list가
# lastGas를 i번 rotate한 누적합과 같다.
# 누적합이 모두 0 이상이 되어야 하므로 누적합에서 가장 작은 원소 index만큼 rotate 해야
# 가장 유리할 것이다.
# 따라서 minVal에 누적합의 최솟값을 저장한 다음, 이 index의 다음 값을 시작점으로 지정한다.
# 만약 모든 원소의 합이 0보다 작으면 누적합 진행 시 0으로 내려가는 구간이 생기게 되므로 
# 불가능한 경우다. 따라서 -1을 반환한다.



class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        lastGas = [g-c for g, c in zip(gas, cost)]

        minVal = (lastGas[0], 0)
        for i in range(1, len(lastGas)):
            lastGas[i] += lastGas[i-1]
            if lastGas[i] < minVal[0]: minVal = (lastGas[i], i)

        if lastGas[-1] < 0: return -1
        return (minVal[1]+1) % len(lastGas)