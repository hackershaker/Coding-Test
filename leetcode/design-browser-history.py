class BrowserHistory:
    class Site:
        def __init__(self, url, prev, next) -> None:
            self.url = url
            self.prev = prev
            self.next = next

    def __init__(self, homepage: str):
        self.node = BrowserHistory.Site(homepage, None, None)
        

    def visit(self, url: str) -> None:
        newnode = BrowserHistory.Site(url, self.node, None)
        self.node.next = newnode
        self.node = newnode
        

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.node.prev:
                self.node = self.node.prev
            else:
                return self.node.url
        return self.node.url
        

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.node.next:
                self.node = self.node.next
            else:
                return self.node.url
        return self.node.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)