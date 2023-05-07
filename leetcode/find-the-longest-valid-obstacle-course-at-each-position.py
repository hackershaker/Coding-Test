from bisect import bisect_right
from typing import List


class Solution:
    def __init__(self) -> None:
        self.arr = []
        self.answer = []

    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        for obstacle in obstacles:
            idx = bisect_right(self.arr, obstacle)
            if idx >= len(self.arr):
                self.arr.append(obstacle)
            elif self.arr[idx] == obstacle:
                self.arr.insert(idx, obstacle)
            else:
                self.arr[idx] = min(obstacle, self.arr[idx])
            self.answer.append(idx + 1)

        return self.answer

