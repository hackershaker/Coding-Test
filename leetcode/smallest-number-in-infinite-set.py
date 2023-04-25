from collections import deque


class SmallestInfiniteSet:
    def __init__(self):
        self.arr = deque([1])

    def popSmallest(self) -> int:
        if len(self.arr) == 1:
            self.arr.append(self.arr[-1] + 1)
        return self.arr.popleft()

    def addBack(self, num: int) -> None:
        if num in self.arr or self.arr[-1] < num:
            return
        start, end = 0, len(self.arr) - 1
        while start < end:
            mid = int((start + end) / 2)
            if self.arr[mid] < num:
                start = mid + 1
            else:
                end = mid
        self.arr.insert(start, num)
        return


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
