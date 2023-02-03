# 규칙을 파악하여 numdic에 차례대로 문자 저장


from collections import defaultdict


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # numRows = n, wave = 2*n - 1
        if numRows == 1: return s
        answer = ''
        numdic = defaultdict(str)

        offset = 0
        while True:
            try:
                for i in range(numRows-1):
                    # print(offset * (2*numRows-2) + i)
                    numdic[i] += s[offset * (2*numRows-2) + i]
                for j in range(numRows-1):
                    # print(offset * (2*numRows-2) + numRows-1 + j)
                    numdic[numRows-1 - j] += s[offset * (2*numRows-2) + numRows-1 + j]
                offset += 1
            except:
                break
        
        for i in range(numRows): answer += numdic[i]
        return answer
        
        