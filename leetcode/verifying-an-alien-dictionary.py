# 순회를 돌면서 순서대로 사전식 배열이 일치하는지 검사


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {char:index for index, char in enumerate(order)}

        for k in range(len(words)-1):
            a, b = words[k], words[k+1]

            i = 0
            while i < max(len(a), len(b)):
                try:
                    if dic[a[i]] < dic[b[i]]: break
                    if dic[a[i]] > dic[b[i]]: return False
                except:
                    if len(a) > len(b): return False
                    else: break
                i += 1

        return True