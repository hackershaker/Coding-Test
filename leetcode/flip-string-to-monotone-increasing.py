# 앞쪽 window와 뒷쪽 window의 counter 이용
# 앞쪽 counter의 1과 뒷쪽 counter의 0을 flip시켜야 하므로
# 순회하면서 두 합의 최솟값 구함


from collections import Counter


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        backCounter = Counter(s)
        answer = backCounter["0"]
        frontCounter = {"0":0, "1":0}

        for i in range(len(s)):
            frontCounter[s[i]] += 1
            backCounter[s[i]] -= 1
            answer = min(answer, frontCounter["1"]+backCounter["0"])

        return answer