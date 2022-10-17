def solution(common):
    if common[2]-common[1] != common[1]-common[0]:
        return common[0] * (common[1] / common[0]) ** len(common)
    else:
        return common[0] + (common[1] - common[0]) * len(common)