class Trie:
    class Node:
        def __init__(self, value, isend: bool) -> None:
            self.value = value
            self.isend = isend
            self.next = {}

    def __init__(self) -> None:
        self.root = Trie.Node(None, False)

    def insert(self, string):
        curnode = self.root
        for s in string:
            if s in curnode.next:
                curnode = curnode.next[s]
            else: 
                newnode = Trie.Node(s, False)
                curnode.next[s] = newnode
                curnode = curnode.next[s]
        else:
            curnode.isend=False

    def find(self, word):
        curnode = self.root
        for w in word:
            if w in curnode.next:
                curnode = curnode.next[w]
            else:
                return False
        return True

    def __repr__(self) -> str:
        return ''

test = ["abc", "abf", "bcd", "csf", "csv"]
trie = Trie()

for word in test:
    trie.insert(word)

trie.find("abc")
trie.find("abf")
trie.find("abk")
trie.find("bcd")
trie.find("csf")
trie.find("csv")
trie.find("bc")