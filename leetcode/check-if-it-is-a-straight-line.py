class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        angle = set()
        for i in range(1, len(coordinates)):
            if coordinates[0][0] == coordinates[i][0]:
                angle.add(float("inf"))
            else:
                angle.add(
                    (coordinates[0][1] - coordinates[i][1])
                    / (coordinates[0][0] - coordinates[i][0])
                )
            if len(angle) > 1:
                return False
        return True
