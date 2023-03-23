from collections import defaultdict


class Solution:
    def __init__(self) -> None:
        self.unionSet = []

    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        self.unionSet = [-1] * n
        for connection in connections:
            a, b = connection
            if self.unionSet[a] == -1 and self.unionSet[b] == -1:
                self.unionSet[a] = self.unionSet[b] = min(a, b)
            elif (self.unionSet[a] == -1) ^ (self.unionSet[b] == -1):
                if self.unionSet[a] == -1:
                    self.unionSet[a] = self.find(b)
                if self.unionSet[b] == -1:
                    self.unionSet[b] = self.find(a)
            else:
                self.union(a, b)

        counter = defaultdict(int)
        unConnectedComputer = 0
        for i in range(n):
            if self.unionSet[i] == -1:
                unConnectedComputer += 1
            else:
                counter[self.find(i)] += 1
        return unConnectedComputer + len(counter.keys()) - 1

    def makeSet(self, x):
        self.unionSet[x] = self.find(x)

    def find(self, x):
        if self.unionSet[x] == x:
            return x
        self.unionSet[x] = self.find(self.unionSet[x])
        return self.unionSet[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        self.unionSet[y] = x
