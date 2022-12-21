from lib2to3.pgen2.pgen import DFAState


# dictionary에 dislike set 들을 저장
# dictionary의 한 key와 있으면 안되는 숫자들 set에 저장
# stack에 이 숫자들을 넣고 dfs진행
# 만약 한 set에 dislike 숫자들이 들어있다면 False
# 모든 dictionary의 key에 대해 진행했을 때 이상이 없다면 True


from collections import defaultdict


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        setA, setB = set(), set()
        dic = defaultdict(list)
        for dislike in dislikes:
            dic[dislike[0]].append(dislike[1])
            dic[dislike[1]].append(dislike[0])

        while dic.keys():
            stack = [list(dic.keys())[0]]

            while stack:
                key = stack.pop()
                for num in dic[key]:
                    if (num in setA and key in setA) or (num in setB and key in setB): return False
                    else:
                        if key in setA: setB.add(num)
                        elif key in setB: setA.add(num)
                        else:
                            setA.add(key)
                            setB.add(num)
                    stack.append(num)
                del dic[key]
        
        return True