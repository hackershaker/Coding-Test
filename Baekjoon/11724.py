# dfs로 연결되어 있는 모든 노드를 방문하고
# answer(연결요소)에 1을 추가



from collections import defaultdict
import sys


class Solution:
    def connectedComponent(self):
        n, m = map(int, sys.stdin.readline().rstrip().split(" "))
        dic = defaultdict(list)
        for _ in range(m):
            u, v = map(int, sys.stdin.readline().rstrip().split(" "))
            dic[u].append(v); dic[v].append(u)

        answer = 0
        visited = set()
        for i in range(1, n+1):
            if i not in visited:
                stack = [i]
                while stack:
                    node = stack.pop()
                    visited.add(node)
                    for nextnode in dic[node]:
                        if nextnode not in visited:
                            stack.append(nextnode)
                            visited.add(nextnode)
                answer += 1

        return answer

def solution():
    s = Solution()
    answer = s.connectedComponent()
    print(answer)

if __name__=="__main__":
    s = Solution()
    answer = s.connectedComponent()
    print(answer)