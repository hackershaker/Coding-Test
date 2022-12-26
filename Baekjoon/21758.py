# 벌통이 양쪽 끝에 있는 경우와 가운데 있는 경우를 고려
# 벌통이 양쪽 끝에 있는 경우 벌 한마리는 무조건 반대 끝에서 시작하는게 많은 꿀을 더할 수 있음
# 나머지 한 마리는 양쪽 끝을 고려한 칸에 있을 경우를 계산해 최댓값 갱신
# 구간합을 빠르게 구하기 위해 prefix sum 이용

def solution():
    n = int(input())
    honey = list(map(int, input().split(" ")))

    s = sum(honey)
    answer = s-honey[0]-honey[-1]+max(honey[1:-1])

    leftPrefixSum = [honey[0]]
    for i in range(1, n): leftPrefixSum.append(leftPrefixSum[i-1]+honey[i])

    rightPrefixSum = [honey[-1]] * n
    for i in range(n-2, -1, -1): rightPrefixSum[i] = rightPrefixSum[i+1] + honey[i]

    for k in range(1,n-1):
        answer = max(answer, s - honey[0] + rightPrefixSum[k] - 2 * honey[k], s - honey[-1] + leftPrefixSum[k] - 2 * honey[k])

    return answer


if __name__=="__main__":
    answer = solution()
    print(answer)