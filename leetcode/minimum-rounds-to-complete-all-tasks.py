# task[i]를 2x+3y(x >= 0, y >= 0)꼴로 나타낼 수 있는지를 물어보는 문제
# 2 이상 자연수이면 모두 이 꼴로 나타낼 수 있다
# 그렇다면 최솟값은? 최대한 y가 큰 게 유리할 것이다.
# 따라서 3으로 나눈 나머지를 조사한다.
# 나머지가 0이면 3으로 나눈 몫이 최솟값
# 나머지가 1이면 (3으로 나눈 몫-1 + (나머지 4를 2+2로 나타낸)2)가 최솟값
# 나머지가 2이면 (3으로 나눈 몫 + 1) 이 최솟값
# 그런데 task[i]가 1이면 2x+3y꼴이 불가능하므로 -1 리턴



from collections import defaultdict


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        dic = defaultdict(int)
        answer = 0

        for task in tasks:
            dic[task] += 1

        for level in dic.keys():
            if dic[level] == 1: return -1
            
            m, r = divmod(dic[level], 3)
            if r == 0: answer += m
            else: answer += (m) + 1

        return answer