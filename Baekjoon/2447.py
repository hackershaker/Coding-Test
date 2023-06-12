import sys
from typing import List


class Solution:
    def solution(self):
        arr = self.makeStarPattern(int(sys.stdin.readline().strip()))
        for row in arr:
            for element in row:
                if element > 0:
                    sys.stdout.write("*" * element)
                else:
                    sys.stdout.write(" " * -element)
            sys.stdout.write("\n")
        return

    def makeStarPattern(self, n: int) -> List[List[int]]:
        if n == 3:
            return [[3], [1, -1, 1], [3]]
        array = self.makeStarPattern(n // 3)
        firstRow = [row * 3 for row in array]
        middleRow = [row + [-n // 3] + row for row in array]

        result = []
        for row in firstRow:
            result.append(row)
        for row in middleRow:
            result.append(row)
        for row in firstRow:
            result.append(row)
        return result


if __name__ == "__main__":
    s = Solution()
    s.solution()
