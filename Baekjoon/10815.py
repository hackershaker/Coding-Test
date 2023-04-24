import sys


class Solution:
    def solution(self):
        answer = []
        n = int(sys.stdin.readline().strip())
        n_deck = sorted(list(map(int, sys.stdin.readline().strip().split(" "))))
        m = int(sys.stdin.readline().strip())
        m_deck = list(map(int, sys.stdin.readline().strip().split(" ")))

        for i in range(m):
            start, end = 0, n - 1
            while start <= end:
                mid = int((start + end) / 2)
                if n_deck[mid] == m_deck[i]:
                    answer.append(1)
                    break
                elif n_deck[mid] > m_deck[i]:
                    end = mid - 1
                else:
                    start = mid + 1
            if len(answer) < i + 1:
                answer.append(0)

        sys.stdout.write(" ".join(map(str, answer)) + "\n")


if __name__ == "__main__":
    s = Solution()
    s.solution()
