# dp 이용
# 가장 큰 subarray의 마지막 index가 현재 검사하는 index와 연결된다면
# 최댓값에 현재 index를 추가한 값이 최댓값
# 아니라면 현재 index부터 역순으로 가장 큰 sub-array 찾아 등록


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dic = {0: {"kind": {fruits[0]}, "indexes": (0, 0)}}  # kind of fruit, start&end

        for i in range(1, len(fruits)):
            if dic[i - 1]["indexes"][1] == i - 1 and (
                fruits[i] in dic[i - 1]["kind"] or len(dic[i - 1]["kind"]) < 2
            ):
                dic[i] = {
                    "kind": dic[i - 1]["kind"] | {fruits[i]},
                    "indexes": (dic[i - 1]["indexes"][0], i),
                }
            else:
                basket = set()
                pick = 0
                for k in range(i, -1, -1):
                    if len(basket) == 2 and fruits[k] not in basket:
                        break
                    basket.add(fruits[k])
                    pick += 1
                    # print(k, basket)
                if pick >= dic[i - 1]["indexes"][1] - dic[i - 1]["indexes"][0] + 1:
                    dic[i] = {"kind": basket, "indexes": (i - pick + 1, i)}
                else:
                    dic[i] = dic[i - 1]
            # pprint(dic)

        start, end = dic[len(fruits) - 1]["indexes"]
        return end - start + 1
