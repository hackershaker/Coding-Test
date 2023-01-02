# 모두 대문자인 경우
# 모두 소문자인 경우
# 가장 앞 글자만 대문자이고 나머지 소문자인 경우
# 3가지 문자열을 구한 후 원래 문자와 비교하여 일치하는 게 있으면 True 반환


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        for i in range(len(word)):
            allUpper = word.upper()
            allLower = word.lower()
            firstUpper = allLower[0].upper() + allLower[1:]

            return True if (allUpper == word or allLower == word or firstUpper == word) else False