# judgeCandidate에 믿는 사람이 n-1인 번호 저장
# notJudge에는 누군가를 믿는 사람들을 저장
# notJudge에 들어가 있지 않은 judgeCandidate 원소 반환


from collections import defaultdict


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1: return 1
        dic = defaultdict(set)
        judgeCandidate = set()
        notJudge = set()

        for a,b in trust:
            dic[b].add(a)
            notJudge.add(a)
            if len(dic[b]) == n-1: judgeCandidate.add(b)

        for candidate in judgeCandidate:
            if candidate not in notJudge:
                return candidate
        return -1