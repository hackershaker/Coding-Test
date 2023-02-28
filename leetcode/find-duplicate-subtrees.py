from collections import defaultdict
from typing import List, Optional


class Solution:
    def __init__(self) -> None:
        self.subtree = defaultdict(int)
        self.hashCodeandNode = {}

    def findDuplicateSubtrees(
        self, root: Optional[TreeNode]
    ) -> List[Optional[TreeNode]]:
        answer = []
        self.getHashCode(root)
        # print(self.subtree)

        for tree in self.subtree:
            if self.subtree[tree] > 1:
                answer.append(self.hashCodeandNode[tree])

        return answer

    def getHashCode(self, root) -> tuple:
        if not root:
            return (None,)
        hashCode = (
            (root.val,) + self.getHashCode(root.left) + self.getHashCode(root.right)
        )
        root.hashCode = hashCode
        self.subtree[root.hashCode] += 1
        self.hashCodeandNode[root.hashCode] = root
        return root.hashCode
