class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        answer = 0
        visited=set()
        for i in range(n):
            if i in visited: continue
            stack =[i]
            while stack:
                node=stack.pop()
                visited.add(node)
                for next in range(len(isConnected[node])):
                    if next in visited or isConnected[node][next]==0:
                        continue
                    stack.append(next)
            answer+=1
        return answer