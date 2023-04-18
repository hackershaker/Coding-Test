import sys


class Solution:
    def solution(self):
        n = int(sys.stdin.readline().strip())
        pinaryNumArray = [{0: 0, 1: 1}]

        for i in range(1, n):  # 2자리부터 n자리까지 구하기
            pinaryNumArray.append({})
            pinaryNumArray[i][0] = pinaryNumArray[i - 1][0] + pinaryNumArray[i - 1][1]
            pinaryNumArray[i][1] = pinaryNumArray[i - 1][0]

        answer = pinaryNumArray[n - 1][0] + pinaryNumArray[n - 1][1]
        print(answer)
        return answer


if __name__ == "__main__":
    s = Solution()
    s.solution()
