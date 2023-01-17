class Solution:
    def solution(self):
        dic = {0:0, 1:1, 2:3}
        n = int(input())
        for i in range(3, n+1):
            dic[i] = dic[i-2]*2 + dic[i-1]

        return dic[n]

if __name__=="__main__":
    s = Solution()
    answer = s.solution()
    print(answer) if answer < 10007 else print(answer % 10007)