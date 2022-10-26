from pprint import pprint
from functools import cmp_to_key
def solution(n, info):
    maxanswer = []
        
    calculate(0, [0 for _ in range(11)], maxanswer, n, info)
    # pprint(maxanswer)
    if len(maxanswer)==0: return [-1]
    else:
        maxanswer = sorted(list(zip(*maxanswer))[0], key = cmp_to_key(compare))
        print(maxanswer)
        return maxanswer[0]

def calculate(i, lion, answer, n, info):
        # print(lion)
        remainarrow = n - sum(lion)
        # print(f"index: {i}, lion's arrow: {lion}")
        if remainarrow == 0:
            # print("remain arrow is 0")
            lionscore = sum([10 - idx for idx in range(11) if lion[idx] > info[idx]])
            apeachscore = sum([10 - idx for idx in range(11) if lion[idx] <= info[idx] and info[idx]>0])
            if lionscore > apeachscore:
                scorediff = lionscore - apeachscore
                # print(f"{lion} score difference is {scorediff}")
                if len(answer)==0 or answer[0][1] == scorediff:
                    answer.append((lion, scorediff))
                elif answer[0][1] < scorediff:
                    answer.clear()
                    answer.append((lion, scorediff))
                else:
                    pass
                # print(answer)
            return

        if i >= 11: return
        calculate(i+1, lion[:i] + [0] + lion[i+1:], answer, n, info)
        calculate(i+1, lion[:i] + [min(remainarrow, info[i]+1)] + lion[i+1:], answer, n, info)

def compare(x, y):
    for i in reversed(range(len(x))):
        if x[i] > y[i]:
            return -1
        elif x[i] < y[i]:
            return 1
        else:
            continue

    return 0
