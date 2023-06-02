from collections import defaultdict


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        dic = defaultdict(list)
        for i in range(len(bombs)):
            for j in range(i + 1, len(bombs)):
                dist = (
                    (bombs[i][0] - bombs[j][0]) ** 2 + (bombs[i][1] - bombs[j][1]) ** 2
                ) ** 0.5
                if dist <= bombs[i][2]:
                    dic[i].append(j)
                if dist <= bombs[j][2]:
                    dic[j].append(i)

        deto = [0] * len(bombs)

        def explore(k, visited):
            visited.add(k)
            for next in dic[k]:
                if next in visited:
                    continue
                explore(next, visited)
            return len(visited)

        for i in range(len(bombs)):
            deto[i] = explore(i, set())

        return max(deto)
