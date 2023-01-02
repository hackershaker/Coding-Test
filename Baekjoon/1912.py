# n이 100,000이나 되기 때문에 효율적인 알고리즘 필요
# 관찰 중 연속합을 끝나는 인덱스로 분류하게 됨.
# 인덱스 0에서 시작해 인덱스 i로 끝나는 연속합을 S(i)라고 하면
# 인덱스 i로 끝나는 연속합은 S(i) - S(k) (0 <= k < i)이 된다.
# 그렇다면 이 연속합이 최대가 되려면 S(k)가 최소여야 한다(S(i)는 고정).

# Prefix Sum을 이용해 S(i)를 구하고
# S(i) 가 기존의 최소값보다 작으면 최소값 갱신
# 기존 최대값, 연속합(S(i)-최솟값), S(i) 중에 최댓값 갱신 



def solution():
    n = int(input())
    numlist = list(map(int, input().split(" ")))
    answer = 0
    
    prefixSum = [numlist[0]]
    for i in range(1, len(numlist)):
        prefixSum.append(prefixSum[i-1] + numlist[i])
    # print(prefixSum)

    minSum = float("inf")
    for i in range(len(numlist)):
        if i == 0:
            minSum = min(minSum, prefixSum[i])
            answer = numlist[i] if i == 0 else max(answer, prefixSum[i]-minSum)
        else:
            answer = max(answer, prefixSum[i]-minSum, prefixSum[i])
            minSum = min(minSum, prefixSum[i])
        # print(minSum, answer)

    return answer

if __name__=="__main__":
    answer = solution()
    print(answer)