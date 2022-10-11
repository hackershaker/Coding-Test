#최소 2가지 이상의 단품메뉴
#최소 2명 이상의 손님으로부터 주문된 단품메뉴
from itertools import combinations
def solution(orders, course):
    answer = []
    def isinmenu(menu, bigmenu):
        for m in menu:
            if m not in bigmenu: return False
        return True
    
    def isincludedmenu(menu, list):
        for bigmenu in list:
            if isinmenu(menu, bigmenu): return True
        return False

    while course:
        temp = []; maxnum = 0
        cnum = course.pop()
        for order in orders:
            if len(order) < cnum: continue
            for menu in combinations(order, cnum):
                menu = ''.join(menu)
                # print(list(map(isinmenu, [menu]*len(orders), orders)), menu)
                # print(f"Is {menu} in {answer}?")
                menucount = list(map(isinmenu, [menu]*len(orders), orders)).count(True)
                if menucount >= 2 and isincludedmenu(menu, temp) == False:
                    # print(menu, menucount)
                    if menucount > maxnum:
                        maxnum = menucount
                        temp = [''.join(sorted(menu))]
                    elif menucount == maxnum:
                        temp.append(''.join(sorted(menu)))
                    else:
                        pass
        # print(temp)
        answer += temp
    return sorted(answer)

# print(solution(	["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]), ["AC", "ACDE", "BCFG", "CDE"])
# print(solution(	["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]), ["AC", "ACDE", "BCFG", "CDE"])
print(solution(	["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]), ["ACD", "AD", "ADE", "CD", "XYZ"])
# print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]), 	["WX", "XY"])