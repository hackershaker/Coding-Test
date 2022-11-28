from typing import List
from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        answer = [[], []]
        playerDict = defaultdict(lambda: [0,0])

        for winner, loser in matches:
            playerDict[winner][0] += 1
            playerDict[loser][1] += 1

        for player, score in playerDict.items():
            if score[0] >= 1 and score[1] == 0:
                answer[0].append(player)
            if score[1] == 1:
                answer[1].append(player)

        return [sorted(answer[0]), sorted(answer[1])]