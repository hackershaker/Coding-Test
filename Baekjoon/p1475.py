from collections import Counter
import math
import sys


class Solution:
    def solution(self):
        dic = Counter(sys.stdin.readline().strip())
        dic["6"] = math.ceil((dic.get("6",0) + dic.get("9",0))/2)
        dic.pop("9", None)

        print(max(dic.values()))


if __name__ == "__main__":
    s = Solution()
    s.solution()
