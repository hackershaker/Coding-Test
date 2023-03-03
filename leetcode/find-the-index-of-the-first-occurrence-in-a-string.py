class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for hIdx in range(len(haystack)):
            if hIdx + len(needle) > len(haystack):
                return -1
            for nIdx in range(hIdx, len(needle) + hIdx):
                if haystack[nIdx] != needle[nIdx - hIdx]:
                    break
            else:
                return hIdx
        return -1
