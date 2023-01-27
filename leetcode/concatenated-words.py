# word를 길이가 작은 순으로 정렬
# 길이가 같거나 크면 다른 단어 속에 있을 수 없다(word는 unique하다는 조건)
# 단어마다 순회를 돌며 인덱스 0부터 dictionary에 포함되는지 검사
# 만약 포함된다면 나머지 stirng이 Concatenated 되어 있는지 재귀로 검사
# 맞다면 answer에 추가



from typing import Concatenate, List


class Solution:
    def __init__(self) -> None:
        self.dictionary = set()

    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key=len)

        answer = set()
        for word in words:
            self.dictionary.add(word)
    
            temp = ""
            for i in range(len(word)-1):
                temp += word[i]
                if temp in self.dictionary:
                    if self.isConcatenate(word[i+1:]):
                        answer.add(word)
                        break
    
        return answer

    def isConcatenate(self, string) -> bool:
        temp = ""

        if not string: return True

        for i in range(len(string)):
            temp += string[i]
            if temp in self.dictionary:
                if self.isConcatenate(string[i+1:]): return True

        return False
