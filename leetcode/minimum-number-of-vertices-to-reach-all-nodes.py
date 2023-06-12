class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        in_degree = [0] * n
        for _, y in edges:
            in_degree[y] += 1

        return [i for i in range(len(in_degree)) if in_degree[i] == 0]
