class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [0] * (len(questions) + 1)

        for i in range(len(questions)):
            point, nextQuestion = questions[i]
            dp[i + 1] = max(dp[i + 1], dp[i])
            try:
                dp[i + nextQuestion + 2] = max(
                    dp[i + nextQuestion + 2], dp[i + 1] + point
                )
            except:
                pass

        # print([questions[i][0]+dp[i+1] for i in range(len(questions))])
        return max([questions[i][0]+dp[i+1] for i in range(len(questions))])
