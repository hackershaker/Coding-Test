import sys


class Solution:
    def solution(self):
        n = int(sys.stdin.readline().strip())
        heap = MinHeap()
        for _ in range(n):
            k = int(sys.stdin.readline().strip())
            if k == 0:
                sys.stdout.write(str(heap.pop()) + "\n")
            else:
                heap.push(k)


class MinHeap:
    def __init__(self) -> None:
        self.heap = []

    def pop(self) -> int:
        if not self.heap:
            return 0
        self.heap[0], self.heap[len(self.heap) - 1] = (
            self.heap[len(self.heap) - 1],
            self.heap[0],
        )
        result = self.heap.pop()
        index = 0
        while index < len(self.heap):
            leftChild, rightChild = index * 2 + 1, index * 2 + 2
            if leftChild < len(self.heap) and rightChild < len(self.heap):
                child = (
                    leftChild
                    if self.heap[leftChild] < self.heap[rightChild]
                    else rightChild
                )
                if self.heap[index] <= self.heap[child]:
                    break
                self.heap[index], self.heap[child] = self.heap[child], self.heap[index]
                index = child
            elif leftChild < len(self.heap) or rightChild < len(self.heap):
                child = leftChild if leftChild < len(self.heap) else rightChild
                if self.heap[index] <= self.heap[child]:
                    break
                self.heap[index], self.heap[child] = self.heap[child], self.heap[index]
                index = child
            else:
                break
        return result

    def push(self, x):
        self.heap.append(x)
        index = len(self.heap) - 1
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[parent] <= self.heap[index]:
                break
            self.heap[parent], self.heap[index] = (
                self.heap[index],
                self.heap[parent],
            )
            index = parent
        return


if __name__ == "__main__":
    s = Solution()
    s.solution()
