from collections import Counter
import sys


class Solution:
    def solution(self):
        n = int(sys.stdin.readline().strip())
        arr = [int(sys.stdin.readline().strip()) for _ in range(n)]

        print(round(sum(arr) / n))
        arr.sort()
        print(arr[n // 2])
        counter = Counter(arr).most_common()
        if len(counter) == 1 or counter[0][1] != counter[1][1]:
            print(counter[0][0])
        else:
            counter.sort(key=lambda x: (-x[1], x[0]))
            print(counter[1][0])
        print(arr[-1] - arr[0])


if __name__ == "__main__":
    s = Solution()
    s.solution()
