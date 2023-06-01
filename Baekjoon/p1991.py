import sys


class Solution:
    def solution(self):
        n = int(sys.stdin.readline().strip())
        tree = {}
        for i in range(n):
            parent, leftnode, rightnode = sys.stdin.readline().strip().split(" ")
            tree[parent] = {"left": leftnode, "right": rightnode}

        print(self.preorder(tree, "A"))
        print(self.inorder(tree, "A"))
        print(self.postorder(tree, "A"))

    def preorder(self, tree: dict, root: str):
        if root == ".":
            return ""
        return (
            root
            + self.preorder(tree, tree[root]["left"])
            + self.preorder(tree, tree[root]["right"])
        )

    def inorder(self, tree, root):
        if root == ".":
            return ""
        return (
            self.inorder(tree, tree[root]["left"])
            + root
            + self.inorder(tree, tree[root]["right"])
        )

    def postorder(self, tree, root):
        if root == ".":
            return ""
        return (
            self.postorder(tree, tree[root]["left"])
            + self.postorder(tree, tree[root]["right"])
            + root
        )


if __name__ == "__main__":
    s = Solution()
    s.solution()
