class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        num = 1
        i = 0
        answer = []
        while len(answer) < k:
            if i >= len(arr) or i < len(arr) and num != arr[i]:
                answer.append(num)
            else:
                i += 1
            num += 1
        return answer[-1]
