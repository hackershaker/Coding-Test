import sys


class Solution:
    def solution(self):
        string = sys.stdin.readline().strip()
        print(
            1
            if all(
                [
                    string[i] == string[len(string) - i - 1]
                    for i in range(len(string) // 2)
                ]
            )
            else 0
        )


if __name__ == "__main__":
    s = Solution()
    s.solution()
