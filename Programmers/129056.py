def solution(babbling):
    answer = 0
    for bab in babbling:
        lastword = ''

        while babbling:
            if bab[:2] in {'ye', 'ma'} and bab[:2] != lastword:
                lastword = bab[:2]
                bab = bab[2:]
            elif bab[:3] in {'aya', 'woo'} and bab[:3] != lastword:
                lastword = bab[:3]
                bab = bab[3:]
            elif bab[:2] in {'ye', 'ma'} and bab[:2] == lastword:
                break
            elif bab[:3] in {'aya', 'woo'} and bab[:3] == lastword:
                break
            else:
                break
        
        if len(bab)==0: answer += 1

    return answer

print(solution(["aya", "yee", "u", "maa"]), 1)
print(solution(["ayay", "yee", "woom", "aye"]), 0)
print(solution(["woowoowoo", "yewoomayeye", "mawooma", "ma"]), 3)