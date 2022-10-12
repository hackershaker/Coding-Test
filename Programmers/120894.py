def solution(numbers):
    answer = ''
    dic = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'zero':0}

    temp = ''
    for i in range(len(numbers)):
        temp += numbers[i]
        if temp in dic.keys():
            answer += str(dic[temp])
            temp = ''
    return int(answer)