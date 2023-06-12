from collections import defaultdict, deque
import sys
class Solution:
    def __init__(self):
        self.dic = defaultdict(list)
        self.n = int(sys.stdin.readline().strip())
        self.a, self.b = sys.stdin.readline().strip().split(" ")
        for _ in range(int(sys.stdin.readline().strip())):
            x,y = sys.stdin.readline().strip().split(" ")
            self.dic[x].append(y)
            self.dic[y].append(x)

    def solution(self):
        stack = deque([(self.a,0)])
        visited = set()
        while stack:
            node, chon = stack.popleft()
            if node == self.b:
                print(chon)
                return
            visited.add(node)
            for next in self.dic[node]:
                if next not in visited:
                    stack.append((next, chon+1))
        print(-1)

if __name__ == '__main__':
    s = Solution()
    s.solution()