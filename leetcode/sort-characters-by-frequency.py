from collections import defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        dic = defaultdict(int)
        answer = ''

        for word in s:
            dic[word] += 1

        for item in sorted(dic.items(), key=lambda x: -x[1]):
            answer += item[0] * int(item[1])

        return answer