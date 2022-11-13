class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()

        answer = []
        temp = ''
        for w in s:
            if w == ' ':
                if temp:
                    answer.append(temp)
                    temp = ''
            else:
                temp += w

        return " ".join(reversed(answer+[temp]))