#최소 2가지 이상의 단품메뉴
#최소 2명 이상의 손님으로부터 주문된 단품메뉴
from itertools import combinations
def solution(orders, course):
    answer = []
    dic = {}
    for coursenumber in course:
        for order in orders:
            for menu in combinations(order, coursenumber): 
                try: dic["".join(menu)] += 1
                except: dic["".join(menu)] = 1
    print(dic)
    for d in dic:
        if dic[d] in course: answer.append(d)
    # print(answer)
    return answer

print(solution(	["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]), [2, 3, 4])
# print(solution(	["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]), [2, 3, 5])
# print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]), [2, 3, 4])