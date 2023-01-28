# 순회를 돌면서 새로운 interval이 겹치는지 조사



from collections import deque
from typing import List, Optional


class SummaryRanges:

    class Node:
        def __init__(self, interval=None, next=None) -> None:
            self.interval = interval
            self.next = next

    def __init__(self):
        self.numJar = set()
        self.interval: Optional[SummaryRanges.Node] = None

    def addNum(self, value: int) -> None:
        if value in self.numJar: return
        self.numJar.add(value)

        # curnode not exists
        if not self.interval:
            self.interval = SummaryRanges.Node(deque([value, value]), None)
        else:
            curnode = self.interval
            if value < curnode.interval[0]-1:
                self.interval = SummaryRanges.Node(deque([value, value]), curnode)
                return

            while True:
                nextnode = curnode.next
                # if previous value can concatenate
                if curnode.interval[0]-1 == value:
                    curnode.interval[0] -= 1
                    return
                if curnode.interval[1]+1 == value:
                    curnode.interval[1] += 1
                    if nextnode != None:
                        if curnode.interval[1]+1 == nextnode.interval[0]:
                            curnode.interval[1] = nextnode.interval[1]
                            curnode.next = nextnode.next
                    return
                if nextnode == None or (nextnode != None and curnode.interval[1]+1 < value and value < nextnode.interval[0]-1):
                    newnode = SummaryRanges.Node(deque([value, value]), nextnode)
                    curnode.next = newnode
                    return
                if nextnode == None: break
                else: curnode = curnode.next

            return

    def getIntervals(self) -> List[List[int]]:
        answer = []
        node = self.interval
        while node:
            answer.append(node.interval)
            node = node.next
        return answer