import sys


class Solution:
    def solution(self):
        n = int(sys.stdin.readline().strip())
        consult = [
            tuple(map(int, sys.stdin.readline().strip().split(" "))) for _ in range(n)
        ]
        stack = [(i, 0) for i in range(n)]
        answer = 0
        while stack:
            time, total = stack.pop()
            if time + consult[time][0] > n:
                continue
            total += consult[time][1]
            answer = max(answer, total)

            for t in range(time + consult[time][0], n):
                stack.append((t, total))
        print(answer)
        return answer


if __name__ == "__main__":
    s = Solution()
    s.solution()
