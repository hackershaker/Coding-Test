import sys


class Solution:
    def solution(self):
        n, k = map(int, sys.stdin.readline().strip().split(" "))
        dic = {}
        for i in range(1, n + 1):
            dic[i] = Node(val=i, prev=i - 1 if i > 1 else n, next=i + 1 if i < n else 1)

        node = Node(val=-1, next=1)
        result = []
        while True:
            for _ in range(k):
                node = dic[node.next]
            result.append(str(node.val))
            dic[node.prev].next = node.next
            dic[node.next].prev = node.prev
            if node.val == node.next:
                break

        print("<" + ", ".join(result) + ">")


class Node:
    def __init__(self, val, prev=None, next=None) -> None:
        self.val = val
        self.prev = prev
        self.next = next


if __name__ == "__main__":
    s = Solution()
    s.solution()
