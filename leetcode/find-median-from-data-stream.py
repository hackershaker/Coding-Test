class MedianFinder:

    def __init__(self):
        self.numlist = []

    def addNum(self, num: int) -> None:
        start = 0; end = len(self.numlist)
        while start < end:
            mid = int((start+end)/2)
            if self.numlist[mid] < num:
                start = mid + 1
            elif self.numlist[mid] > num:
                end = mid
            else:
                self.numlist.insert(mid, num)
                return
        self.numlist.insert(start, num)
        print(self.numlist)

    def findMedian(self) -> float:
        if len(self.numlist) % 2 == 1:
            return self.numlist[int(len(self.numlist)/2)]
        else:
            return (self.numlist[int(len(self.numlist)/2)] + self.numlist[int(len(self.numlist)/2)-1]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
