from itertools import zip_longest


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        a, b, c = bin(a)[2:][::-1], bin(b)[2:][::-1], bin(c)[2:][::-1]
        answer = 0
        for i, j, k in zip_longest(a, b, c, fillvalue="0"):
            if k == "0" and i == "1" and j == "1":
                answer += 1
            if k == "0" and (i == "1" or j == "1"):
                answer += 1
            if k == "1":
                if i == "0" and j == "0":
                    answer += 1
        return answer
