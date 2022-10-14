from collections import deque
def solution(tickets):
    dic = {x[0]: [] for x in tickets}
    for t in tickets:
            dic[t[0]] += t[1:]

    # print(dic)
    path = []
    stack = [(["ICN"], dic)]
    while stack:
        p, pathinfo = stack.pop()
        # print(p, pathinfo)
        if len(p) == len(tickets) + 1:
            path.append(p)
            continue
        try:
            temp = []
            for c in pathinfo[p[-1]]:
                temp.append(c)

            for country in temp:
                l = pathinfo[p[-1]][:]
                l.remove(country)
                newel = {p[-1]: l}
                # print(newel)
                backup = pathinfo[p[-1]]
                del pathinfo[p[-1]]
                # print("update path : ", (p + [country], pathinfo))
                stack.append((p + [country], {**pathinfo , **newel}))
                # print("stack : ", stack)
                pathinfo[p[-1]] = backup
            # print(dic)
        except:
            # print(e)
            continue

    path.sort()
    return path[0]

def solution2(tickets):
    dic = {x[0]: deque([]) for x in tickets}
    for t in tickets:
            dic[t[0]] += t[1:]
            dic[t[0]] = deque(sorted(dic[t[0]]))

    stack = [["ICN"]]
    while stack:
        p = stack.pop()

        for country in dic[p[-1]]:
            stack.append(p + [country])



print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
# print(solution([["ICN", "ATL"], ["ATL", "ICN"], ["ICN", "SFO"], ["SFO", "ATL"], ["ATL","SFO"], ["SFO","DUF"], ["DUF","ICN"], ["ICN", "ZTF"], ["ZTF", "KFC"]]))
# print(solution([["ICN", "AAB"], ["AAB", "ICN"], ["ICN", "AAC"], ["AAC", "ATL"], ["ATL","ICN"], ["ICN","AAE"], ["AAE","ICN"], ["ICN","AAE"], ["AAE","ICN"], ["ICN", "AAF"], ["AAF", "KFC"]]))
# print(solution([["ICN", "SFO"], ["SFO", "ATL"], ["ATL", "ICN"], ["ICN", "SFO"], ["SFO","ATL"], ["ATL", "ICN"]]))
# print(solution([["ICN", "SFO"], ["SFO", "ICN"], ["ICN", "SFO"], ["SFO", "ICN"],["ICN", "SFO"], ["SFO", "ICN"],["ICN", "SFO"], ["SFO", "ICN"],]))
# print(solution([["ICN", "SFO"], ["SFO", "GDP"], ["GDP", "ASG"], ["ASG", "WDF"],["WDF", "XDF"], ["XDF", "AFD"],["AFD", "WDF"], ["WDF", "AGS"],]))