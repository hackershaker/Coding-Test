from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiantTotal = senate.count("R")
        direTotal = len(senate) - radiantTotal
        deq = deque(senate)
        radiantBan, direBan = 0, 0

        while radiantTotal and direTotal:
            if deq[0] == "R":
                if radiantBan > 0:
                    radiantBan -= 1
                    deq.popleft()
                    radiantTotal -= 1
                else:
                    direBan += 1
                    deq.rotate(-1)
            else:
                if direBan > 0:
                    direBan -= 1
                    deq.popleft()
                    direTotal -= 1
                else:
                    radiantBan += 1
                    deq.rotate(-1)

        return "Radiant" if radiantTotal else "Dire"
