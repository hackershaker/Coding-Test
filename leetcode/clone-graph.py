"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def __init__(self) -> None:
        self.nodeDict = dict()

    def cloneGraph(self, node: "Node") -> "Node":
        if not node:
            return None
        if node.val not in self.nodeDict:
            self.nodeDict[node.val] = Node(val=node.val)
        newnode = self.nodeDict[node.val]

        for adjnode in node.neighbors:
            if adjnode.val in self.nodeDict:
                newnode.neighbors.append(self.nodeDict[adjnode.val])
            else:
                newnode.neighbors.append(self.cloneGraph(adjnode))

        return newnode
