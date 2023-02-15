# k에 num의 각 자릿수를 더함
# answer에 차례대로 k의 자릿수를 넣은 다음
# reverse하여 반환


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        for i in reversed(range(len(num))):
            k += num[i] * (10 ** (len(num)-i-1))

        answer = []
        while k:
            k, r = divmod(k, 10)
            answer.append(r)

        return answer[::-1]
            