class Solution:
    def trap(self, height: list[int]) -> int:
        wall = height[0]
        total = 0
        waterIdx = set()
        temp = 0
        tempIdx = []
        for i in range(len(height)):
            if wall > height[i]:
                tempIdx.append(i)
                temp += wall-height[i]
            if wall <= height[i]:
                waterIdx.update(tempIdx)
                wall = height[i]
                total += temp
                temp = 0
                tempIdx.clear()

        wall = height[-1]
        temp = 0
        for j in reversed(range(len(height))):
            if wall > height[j] and j not in waterIdx:
                temp += wall-height[j]
            if wall <= height[j]:
                wall = height[j]
                total += temp
                temp = 0

        return total
