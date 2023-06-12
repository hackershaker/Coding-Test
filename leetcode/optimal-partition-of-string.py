# Greedy


class Solution:
    def partitionString(self, s: str) -> int:
        answer = 0
        basket = set()
        for character in s:
            if character in basket:
                basket = {character}
                answer += 1
            else:
                basket.add(character)
        else:
            if basket:
                answer += 1

        return answer
