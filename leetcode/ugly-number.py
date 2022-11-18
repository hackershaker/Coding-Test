class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0: return False 
        while n > 1:
            # devidedby2, devidedby3, devidedby5 = False, False, False
            if n % 2 == 0:
                n = n // 2
                continue
            if n % 3 == 0:
                n = n // 3
                continue
            if n % 5 == 0:
                n = n // 5
                continue
            return False
        return True
