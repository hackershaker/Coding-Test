def solution(sticker):
    def checkMaxSum(start: int, end: int, array: list):
        dic = {(start,start):sticker[start], (start, start+1): max(sticker[start], sticker[start+1])}

        for i in range(start+2, end+1):
            dic[(start, i)] = max(dic[(start, i-2)] + sticker[i], dic[(start, i-1)])

        return dic[(start, end)]

    if len(sticker) == 1:
        return sticker[0]
    elif 2 <= len(sticker) <= 3:
        return max(sticker)
    else:
        return max(sticker[0] + checkMaxSum(2, len(sticker)-2, sticker), 
        sticker[1] + checkMaxSum(3, len(sticker)-1, sticker), 
        sticker[-1] + checkMaxSum(1, len(sticker)-3, sticker))