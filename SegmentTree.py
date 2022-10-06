class segmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.length = len(arr)
        self.dic = {}
        self.init(1, 0, len(arr) - 1)

    def init(self, node, start, end):
        mid = int((start + end) / 2)
        if start == end:
            self.dic[node] = self.arr[start]
            return self.dic[node]

        self.dic[node] = self.init(node * 2, start, mid) + self.init(
            node * 2 + 1, mid + 1, end
        )
        return self.dic[node]

    def getSum(self, start, end, node, left, right):
        mid = int((start + end) / 2)
        if right < start or end < left:
            return 0
        elif left <= start and end <= right:
            return self.dic[node]
        else:
            return self.getSum(start, mid, node * 2, left, right) + self.getSum(
                mid + 1, end, node * 2 + 1, left, right
            )

    def update(self, start, end, node, idx, value):
        mid = int((start + end) / 2)
        if idx < start or idx > end:
            pass
        if start <= idx and idx <= end:
            self.dic[node] += value
        if start == end:
            return

        return self.update(start, mid, node * 2, idx, value), self.update(
            mid + 1, end, node * 2 + 1, idx, value
        )


segtree = segmentTree([2, 4, 5, 3, 2, 1, 4, 2, 5, 1])
print(sorted(segtree.dic.items()))
print(segtree.getSum(0, len(segtree.arr) - 1, 1, 0, 5))
segtree.update(0, len(segtree.arr) - 1, 1, 0, -1)
print(segtree.getSum(0, len(segtree.arr) - 1, 1, 0, 5))
print(sorted(segtree.dic.items()))
