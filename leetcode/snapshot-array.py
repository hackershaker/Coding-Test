class SnapshotArray:
    def __init__(self, length: int):
        self.arr = {}
        self.snapShot = [[[-1, 0]] for _ in range(length)]
        self.snapId = -1

    def set(self, index: int, val: int) -> None:
        self.arr[index] = val

    def snap(self) -> int:
        self.snapId += 1
        for i in self.arr:
            element = self.arr[i]
            if self.snapShot[i][-1][1] != element:
                # lazy update for same element
                if self.snapShot[i][-1][0] != self.snapId - 1:
                    self.snapShot[i][-1][0] = self.snapId - 1
                self.snapShot[i].append([self.snapId, element])
            else:
                self.snapShot[i][-1][0] = self.snapId
        self.arr = {}
        # print(self.snapShot)
        return self.snapId

    def get(self, index: int, snap_id: int) -> int:
        start, end = 0, len(self.snapShot[index]) - 1
        while start < end:
            mid = (start + end) // 2
            if self.snapShot[index][mid][0] < snap_id:
                start = mid + 1
            else:
                end = mid
        return self.snapShot[index][end][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
