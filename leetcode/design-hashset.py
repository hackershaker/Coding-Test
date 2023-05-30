class MyHashSet:

    def __init__(self):
        self.arr = [[] for _ in range(10**4)]

    def add(self, key: int) -> None:
        if key not in self.arr[self.hash(key)]:
            self.arr[self.hash(key)].append(key)

    def remove(self, key: int) -> None:
        if key in self.arr[self.hash(key)]:
            self.arr[self.hash(key)].remove(key)

    def contains(self, key: int) -> bool:
        if key in self.arr[self.hash(key)]:
            return True
        return False
        
    def hash(self, key:int) -> int:
        return key%100


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)