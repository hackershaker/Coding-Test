from collections import defaultdict


class UndergroundSystem:
    def __init__(self):
        self.stos = defaultdict(
            lambda: defaultdict(lambda: [0, 0])
        )  # total travel number, total travel time
        self.idTrack = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.idTrack[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.idTrack[id]
        self.stos[startStation][stationName][0] += 1
        self.stos[startStation][stationName][1] += t - startTime
        del self.idTrack[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        c, t = self.stos[startStation][endStation]
        return t / c


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
