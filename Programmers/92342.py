from pprint import pprint

def solution(n, info):
    answer = []

    def calculate(i, lion):
        # print(lion)

        remainarrow = n - sum(lion)
        # print(f"index: {i}, lion's arrow: {lion}")
        if remainarrow == 0:
            # print("remain arrow is 0")
            lionscore = sum([10 - i for i in range(11) if lion[i] > info[i]])
            targetscore = sum([10 - i for i in range(11) if lion[i] < info[i]])
            if lionscore > targetscore:
                # print(f"{lion} arrow score is {lionscore}")
                answer.append((lion, lionscore))
            return

        if i >= 11: return
        calculate(i+1, lion[:i] + [0] + lion[i+1:])
        calculate(i+1, lion[:i] + [min(remainarrow, info[i]+1)] + lion[i+1:])
        
    calculate(0, [0 for _ in range(11)])
    # pprint(answer)
    if len(answer)==0: return [-1]
    else: return sorted(answer, key = lambda x : (-x[1], x[0]))[0][0]

# print(solution(1, [0,0,1,0,0,0,0,0,0,0,0,0]), [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
# print(solution(2, [0,0,1,1,0,0,0,0,0,0,0,0]), [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
# print(solution(3, [1,0,1,0,1,0,0,0,0,0,0,0]), [2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
# print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]), [0, 2, 2, 0, 1, 0, 0, 0, 0, 0, 0])
# print(solution(	1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ), 	[-1])
# print(solution(	9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]), [1, 1, 2, 0, 1, 2, 2, 0, 0, 0, 0])
print(solution(	10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]), [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 2])
# print(solution(10, [1,0,1,1,1,1,1,1,1,1,1]))