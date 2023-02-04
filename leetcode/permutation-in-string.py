# counter, sliding window 이용
# s2에 s1의 길이만큼의 window를 움직이면서 counter가 같은지 확인


from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts1 = Counter(s1)
        counts2 = Counter(s2[:len(s1)])
        print(counts1, counts2)
        if counts1 == counts2: return True

        start, end = 0, len(s1)-1
        while end < len(s2):
            try:
                counts2[s2[start]] -= 1
                if counts2[s2[start]] == 0: del counts2[s2[start]]
                start += 1

                end += 1
                counts2[s2[end]] += 1 if s2[end] in counts2 else 1
                if counts1 == counts2: return True
            except: break
        return False