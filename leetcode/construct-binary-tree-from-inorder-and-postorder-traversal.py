# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return self.convertTree(inorder, postorder)

    def convertTree(
        self, inorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
        if not inorder:
            return None
        if len(inorder) == 1:
            return TreeNode(val=inorder[0], left=None, right=None)

        rootValue = postorder[-1]
        rootIndexinInorder = inorder.index(rootValue)
        inorderLeftSubTree = inorder[:rootIndexinInorder]
        inorderRightSubTree = inorder[rootIndexinInorder + 1 :]
        postorderLeftSubTree = postorder[: len(inorderLeftSubTree)]
        postorderRightSubTree = postorder[
            len(inorderLeftSubTree) : len(inorderLeftSubTree) + len(inorderRightSubTree)
        ]
        return TreeNode(
            val=rootValue,
            left=self.convertTree(inorderLeftSubTree, postorderLeftSubTree),
            right=self.convertTree(inorderRightSubTree, postorderRightSubTree),
        )
