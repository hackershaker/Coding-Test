class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area1 = abs(ax1-ax2) * abs(ay1-ay2)
        area2 = abs(bx1-bx2) * abs(by1-by2)

        dup = max(self.computeDupArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2), self.computeDupArea(bx1, by1, bx2, by2, ax1, ay1, ax2, ay2))
        
        print(area1, area2, dup)
        return area1 + area2 - dup

    def computeDupArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int):
        if by1 >= ay2 or by2 <= ay1 or bx1 >= ax2 or bx2 <= ax1:
            return 0
        if ax1 <= bx1 <= ax2:
            if ay2 <= by2 and by1 <= ay1:
                return min(abs(bx1-ax2), abs(bx1-bx2)) * (ay2-ay1)
            if ay1 <= by2 <= ay2:
                return min(abs(bx1-ax2), abs(bx1-bx2)) * min(abs(by2-ay1), abs(by2-by1))
            if ay1 <= by1 <= ay2:
                return min(abs(bx1-ax2), abs(bx1-bx2)) * min(abs(by1-ay2), abs(by1-by2))
        if ax1 <= bx2 <= ax2:
            if ay2 <= by2 and by1 <= ay1:
                return min(abs(bx2-bx1), abs(bx2-ax1)) * (ay2-ay1)
            if ay1 <= by2 <= ay2:
                return min(abs(bx2-bx1), abs(bx2-ax1)) * min(abs(by2-by1), abs(by2-ay1))
            if ay1 <= by1 <= ay2:
                return min(abs(bx2-bx1), abs(bx2-ax1)) * min(abs(by1-by2), abs(by1-ay2))
        if bx1 <= ax1 and not ax2 <= bx2 and ay1 <= by2 <= ay2 and ay1 <= by1 <= ay2:
            return (ax2-ax1) * (by2-by1)

        return 0