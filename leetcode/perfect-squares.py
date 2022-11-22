from collections import deque
class Solution:
    def numSquares(self, n: int) -> int:
        squareNums = [x**2 for x in range(1, 101)]
        numlist = deque([(x**2, 1) for x in range(1, 101)])
        key = {x**2 for x in range(1, 101)}

        while True:
            k, sumcount = numlist.popleft()
            if k == n:
                return sumcount
            for sq in squareNums:
                if k + sq > n: break
                if k + sq not in key:
                    key.add(k + sq)
                    numlist.append((k + sq, sumcount + 1))