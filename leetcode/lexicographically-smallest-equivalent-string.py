# linked list 이용
# next node의 마지막 노드가 바꿀 문자
# 문자가 이미 node를 가지고 있을 경우와 가지고 있지 않을 경우를 계산
# linked list를 다 만들고 baseStr 바꿔서 return

class Solution:
    class Node:
        def __init__(self, val, nextNode=None) -> None:
            self.val = val
            self.next = nextNode

    def getRootNode(self, node:Node) -> Node:
        while True:
            if not node.next:
                return node
            node = node.next
        
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        nodeSet = {}

        for a, b in zip(s1, s2):
            if a == b: continue
            elif a in nodeSet and b not in nodeSet or b in nodeSet and a not in nodeSet:
                if a in nodeSet: a, b = a, b
                else: b, a = a, b

                node = self.getRootNode(nodeSet[a])

                if ord(node.val) < ord(b):
                    newnode = self.Node(b, node)
                    nodeSet[b] = newnode
                elif ord(node.val) > ord(b):
                    newnode = self.Node(b, None)
                    nodeSet[b] = newnode
                    node.next = newnode
                else: continue
            elif a not in nodeSet and b not in nodeSet:
                anode, bnode = self.Node(a), self.Node(b)
                if ord(a) < ord(b):
                    bnode.next = anode
                else:
                    anode.next = bnode
                nodeSet[a] = anode; nodeSet[b] = bnode
            else:
                rootA, rootB = self.getRootNode(nodeSet[a]), self.getRootNode(nodeSet[b])
                if ord(rootA.val) < ord(rootB.val):
                    nodeSet[rootB.val].next = nodeSet[rootA.val]
                elif ord(rootA.val) > ord(rootB.val):
                    nodeSet[rootA.val].next = nodeSet[rootB.val]
                else:
                    continue

        answer = ""

        for c in baseStr:
            if c not in nodeSet:
                answer += c
            else:
                node = self.getRootNode(nodeSet[c])
                answer += node.val

        return answer