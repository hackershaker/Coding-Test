class Trie:
    class Node:
        def __init__(self) -> None:
            self.value = ""
            self.dic = {}

    def __init__(self):
        self.tree = Trie.Node()

    def insert(self, word: str) -> None:
        node = self.tree
        for i in range(len(word)):
            if word[i] in node.dic:
                node = node.dic[word[i]]
            else:
                newnode = Trie.Node()
                node.dic[word[i]] = newnode
                node = newnode
        node.value = word

    def search(self, word: str) -> bool:
        index = 0
        node = self.tree
        while index < len(word):
            if word[index] in node.dic:
                node = node.dic[word[index]]
                index += 1
            else:
                return False
        return True if node.value == word else False

    def startsWith(self, prefix: str) -> bool:
        index = 0
        node = self.tree
        while index < len(prefix):
            if prefix[index] in node.dic:
                node = node.dic[prefix[index]]
                index += 1
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
