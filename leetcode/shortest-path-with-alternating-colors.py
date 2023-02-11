# bfs이용


from collections import OrderedDict, defaultdict, deque


class Solution:
    def __init__(self) -> None:
        # self.edgeDict : (start: end)
        self.edgeDict = None
        # self.colorDict : ((start , end) : color)
        self.colorDict = None

    def shortestAlternatingPaths(
        self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]
    ) -> List[int]:
        answer = [0] + [-1] * (n - 1)
        self.edgeDict = defaultdict(set)
        self.colorDict = defaultdict(list)
        # save edge information and color
        # red = 1, blue = -1
        for edge in redEdges:
            self.edgeDict[edge[0]].add(edge[1])
            self.colorDict[tuple(edge)].append(1)
        for edge in blueEdges:
            self.edgeDict[edge[0]].add(edge[1])
            self.colorDict[tuple(edge)].append(-1)

        visited = OrderedDict({(0, None): 0})  # (node, color) : length
        stack = deque([(0, 0, None)])  # last node, length, color
        while stack:
            lastNode, length, color = stack.popleft()

            for nextNode in self.edgeDict[lastNode]:
                # if lastnode does not have prev edge
                # lastnode is startnode
                if not color:
                    # don't need to consider prev color
                    # because lastnode is start
                    # so update visited and answer
                    for c in self.colorDict[(lastNode, nextNode)]:
                        visited[(nextNode, c)] = length + 1
                        stack.append((nextNode, length + 1, c))
                        answer[nextNode] = (
                            length + 1
                            if answer[nextNode] == -1
                            else min(answer[nextNode], length + 1)
                        )
                # if lastnode have prev edges
                else:
                    # check not visited and alternate color edge
                    # exist in nextnode edges
                    if color * -1 in self.colorDict[(lastNode, nextNode)]:
                        if (nextNode, color * -1) not in visited:
                            visited[(nextNode, color * -1)] = length + 1
                            stack.append((nextNode, length + 1, color * -1))
                            answer[nextNode] = (
                                length + 1
                                if answer[nextNode] == -1
                                else min(answer[nextNode], length + 1)
                            )

        return answer
