import sys


class Solution:
    def solution(self):
        k, n = map(int, sys.stdin.readline().strip().split(" "))
        kLAN = [int(sys.stdin.readline().strip()) for _ in range(k)]

        start, end = 1, 2**31 - 1
        while start < end:
            mid = int((start + end) / 2) + 1
            lanNumber = 0
            for line in kLAN:
                lanNumber += line // mid
            if lanNumber >= n:
                start = mid
            else:
                end = mid - 1
        print(start)
        return start


if __name__ == "__main__":
    s = Solution()
    s.solution()
