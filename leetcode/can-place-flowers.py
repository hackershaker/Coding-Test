from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        newflowerbed = [1, 0]
        newflowerbed.extend(flowerbed)
        newflowerbed.extend([0, 1])
        flowerbed = newflowerbed
        print(flowerbed)

        answer = 0
        empty = 0
        for plant in flowerbed:
            if plant == 1:
                if empty > 0:
                    if empty % 2 == 1:
                        answer += (empty - 1) // 2
                    else:
                        answer += (empty - 2) // 2
                empty = 0
            else:
                empty += 1
        return answer >= n
