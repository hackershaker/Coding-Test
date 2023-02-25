# buy when price is low
# sell when price is high
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        start = 10**4 + 1
        end = -1

        for price in prices:
            # find lower price than current buying point
            if start > price:
                # if there exists increase section
                if end > 0:
                    # renewal this section's information
                    answer = max(answer, end - start)
                    # after renewal, end point not exists
                    # so initialize end
                    end = -1
                start = price
            else:
                # if start doesn't change
                # find end point that has maximum value
                end = max(end, price)

        if end >= 0:
            answer = max(answer, end - start)
        return answer
