# s의 길이만큼 iteration
# 만약 dic에 없는 키이면 s:pattern 식으로 저장
# dic에 있는 키면 해당 pattern 값이 dic의 다른 키의 value가 아닌지 검사
# (dog:a, bird:a 인 경우를 걸러야 하기 때문)
# 즉, value값도 고유해야 한다는 점에 유의
# s 값을 dictionary값으로 바꾼 다음 pattern값과 같지 않으면 False
# 모든 iteration을 끝마쳤으면 True 리턴

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        dic = {}

        if len(s) != len(pattern): return False

        for i in range(len(s)):
            try:
                s[i] = dic[s[i]]
            except:
                if s[i] not in dic.keys() and pattern[i] in dic.values(): return False
                dic[s[i]] = pattern[i]
                s[i] = dic[s[i]]

            if s[i] != pattern[i]: return False

        return True