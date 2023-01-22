# 재귀 함수, backtracking 이용
# slice한 문자가 pelindrome이면 나머지 문자열에 대해 검사 진행


class Solution:
    def __init__(self) -> None:
        self.answer = []

    def partition(self, s: str) -> List[List[str]]:
        return self.subString(s)

    def subString(self, string):
        if len(string)==1: return [[string]]
        if len(string)==0: return None
        result = []

        for i in range(1, len(string)+1):
            subString = string[:i]
            if self.isPalindrome(subString):
                subs = self.subString(string[i:])
                if not subs: result.append([subString])
                else:    
                    for res in subs:
                        result.append([subString] + res)
        return result

    @staticmethod
    def isPalindrome(string):
        for i in range(len(string)//2):
            if string[i] != string[len(string)-1-i]: return False
        return True