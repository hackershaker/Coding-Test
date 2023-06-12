class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        arr = [True] + [None] * (len(graph) - 1)
        
        for i in range(len(graph)):
            stack = [i]
            while stack:
                node = stack.pop()
                for nextnode in graph[node]:
                    if arr[nextnode] == None:
                        arr[nextnode] = not arr[node]
                        stack.append(nextnode)
                    else:
                        if arr[node] == arr[nextnode]:
                            return False

        return True
