from typing import List


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions.sort()
        answer = []

        for spell in spells:
            start, end = 0, len(potions)
            while start < end:
                mid = int((start + end) / 2)
                if potions[mid] * spell >= success:
                    end = mid
                else:
                    start = mid + 1

            answer.append(len(potions)-start)
        return answer
        