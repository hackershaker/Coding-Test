class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        start, end = 1, 500 * 5 * (10**4)

        while start < end:
            mid = int((start + end) / 2)  # capacity limit
            bag = [0] * days
            index = 0

            for weight in weights:
                if weight > mid:
                    break
                if bag[index] + weight <= mid:
                    bag[index] += weight
                else:
                    index += 1
                    if index >= len(bag):
                        break
                    bag[index] += weight
            else:
                # can deliver current capacity,
                # find more less possible capacity
                end = mid
                continue

            # overflow days or
            # there is weight bigger than capacity
            start = mid + 1

        return start
