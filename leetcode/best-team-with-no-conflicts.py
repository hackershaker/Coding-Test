# dp 이용
# age 순서대로 sort해서 무조건 더 크거나 같은 age를 검사하도록 설정
# maxScores에 저장된 총 점수를 순회를 돌면서 조건에 맞으면 최대 점수 갱신
# answer에 최대 점수 갱신


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        answer = 0
        ageandScore = [x for x in zip(ages, scores)] # (age, score)
        ageandScore.sort()

        maxScores = {} # (age, index) : score, total

        for idx, entry in enumerate(ageandScore):
            age, score = entry
            if not maxScores: 
                maxScores[(age, idx)] = (score, score)
                answer = max(answer, score)
            else:
                maxTotal = score
                for keyEntry in maxScores:
                    key, index = keyEntry
                    if key == age or key < age and maxScores[keyEntry][0] <= score:
                        maxTotal = max(maxTotal, maxScores[keyEntry][1] + score)
                maxScores[(age, idx)] = (score, maxTotal)
                answer = max(answer, maxTotal)

        return answer