import sys


class Solution:
    def solution(self):
        paper = [[] for _ in range(101)]
        n = int(sys.stdin.readline().strip())
        for _ in range(n):
            x, y = map(int, sys.stdin.readline().strip().split(" "))
            for i in range(x, x + 10):
                if not paper[i]:
                    paper[i].append((y, y + 10))
                    continue
                paper[i].append((y, y + 10))

        answer = 0
        for j in range(100):
            p = paper[j]
            if p:
                p.sort(key=lambda x: x[0])
                start, end = None, None
                for l, h in p:
                    if start == None:
                        start, end = l, h
                    else:
                        if end < l:
                            answer += end - start
                            start, end = l, h
                        else:
                            end = h
                answer += end - start

        print(answer)


if __name__ == "__main__":
    s = Solution()
    s.solution()

"""
2
5 16
5 90
"""
"""
10
1 1
10 1
20 1
30 1
40 1
50 1
60 1
70 1
80 1
90 1
"""
"""
3
1 2
5 6
3 1
"""
"""
2
3 7
15 7
"""
"""
2
90 90
80 80
"""
"""
2
90 90
89 89
"""
"""
2
0 0
9 9
"""
"""
9
1 2
5 16
7 18
1 0
0 1
5 90
8 77
55 7
23 78
666
"""
