# 순회를 돌면서 newInterval보다 앞쪽 혹은 뒤쪽에 있으면
# answer에 추가하고
# newInterval과 겹치면 newInterval 갱신
# 순회가 끝난 후 newInterval을 answer에 넣고 sort 후 return


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        answer = []
        for i in range(len(intervals)):
            start, end = intervals[i]

            if end < newInterval[0]: answer.append(intervals[i])
            elif newInterval[1] < start:
                answer.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], start), max(newInterval[1], end)]
        
        answer.append(newInterval)
        answer.sort()
        return answer