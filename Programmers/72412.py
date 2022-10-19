import re
def solution(info, query):
    answer = []
    for i in range(len(info)):
        info[i] = info[i].split(" ")

    for q in query:
        q = re.findall("([a-z]+|-) and ([a-z]+|-) and ([a-z]+|-) and ([a-z]+|-) (\d+)", q)[0]
        l = 0
        for x in info:
            if int(x[4]) < int(q[4]): continue
            for i in range(len(q)-1):
                if q[i] == "-": continue
                if (q[i] != x[i]): break
            else:
                l += 1

        answer.append(l)
    return answer

print(solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]), [1, 1, 1, 1, 2, 4])