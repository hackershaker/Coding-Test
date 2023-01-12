# 재귀 구현
# 왼쪽 노드, 오른쪽 노드의 dictionary({인덱스:개수})를 구하고
# 이로부터 answer에 해당 subtree의 index개수 갱신
# root를 포함한 dictionary 반환



from collections import defaultdict


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        answer = [0] * n
        dic = defaultdict(list)
        for edge in edges:
            dic[edge[0]].append(edge[1])
            dic[edge[1]].append(edge[0])

        self.findSameIndex(0, -1, dic, answer, labels)
        return answer

    def findSameIndex(self, root: int, parent: int, dic:dict, answer:list, labels:str):
        dics = [self.findSameIndex(node, root, dic, answer, labels) for node in dic[root] if node != parent]
        if len(dics) == 0:
            answer[root] = 1
            return {labels[root]: 1}

        newdic = dics[0]

        for i in range(1, len(dics)):
            for key in dics[i]:
                if key in newdic.keys():
                    newdic[key] += dics[i][key]
                else:
                    newdic[key] = dics[i][key]

        if newdic.get(labels[root], None) == None:
            newdic[labels[root]] = 1
        else:
            newdic[labels[root]] += 1
        answer[root] = newdic[labels[root]]
        print(answer,newdic)

        return newdic