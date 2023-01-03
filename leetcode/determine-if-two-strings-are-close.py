# prevword에 이전 문자를 저장
# 아스키코드를 사용해 비교 -> prevword의 아스키코드가 더 크다면 
# sorted되지 않았다는 것이므로 answer에 1 추가

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        prevword = ""; answer = 0

        for c in range(len(strs[0])):
            for i in range(len(strs)):
                print(prevword, strs[i][c])
                if i == 0:
                    prevword = strs[0][c]
                else:
                    if ord(prevword) > ord(strs[i][c]):
                        answer += 1
                        break
                    prevword = strs[i][c]

        return answer