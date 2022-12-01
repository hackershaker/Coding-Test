class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a, b = s[:int(len(s)/2)], s[int(len(s)/2):]
        aCounter, bCounter = vowelCounter(), vowelCounter()

        for k, v in zip(a, b):
            if k in aCounter.dic:
                aCounter.dic[k] += 1
            if v in bCounter.dic:
                bCounter.dic[v] += 1
        
        if sum(aCounter.dic.values()) == sum(bCounter.dic.values()): return True
        return False

class vowelCounter():
    def __init__(self):
        self.dic = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0, 'A':0, 'E':0, 'I':0,'O':0, 'U':0,}