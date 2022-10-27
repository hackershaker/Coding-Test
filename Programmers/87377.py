def solution(line):
    cross = []
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            ord = crossord(line[i], line[j])
            if ord == None: continue
            elif not (isInt(ord[0]) and isInt(ord[1])):
                continue
            else:
                cross.append(ord)

    # print(cross)
    minx = min(list(zip(*cross))[0])
    miny = min(list(zip(*cross))[1])
    maxx = max(list(zip(*cross))[0])
    maxy = max(list(zip(*cross))[1])

    row, column = int(maxy-miny+1), int(maxx-minx+1)

    for i in range(len(cross)):
        cross[i] = [int(cross[i][0]-minx), int(cross[i][1]-miny)]
    # print(cross)

    answer = [['.'for _ in range(column)] for _ in range(row)]

    for point in cross:
        answer[row - point[1] - 1][point[0]] = '*'
    # print(answer)
    for k in range(len(answer)):
        answer[k] = "".join(answer[k])

    return answer
    
def crossord(A, B):
    a,b,e = A
    c,d,f = B

    if a*d == b*c: return None
    else:
        return ((b*f - e*d) / (a*d - b*c), (e*c - a*f) / (a*d - b*c))

def isInt(k):
    if int(k) == k:
        return True
    else:
        return False

# print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
# print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))
# print(solution([[1, -1, 0], [2, -1, 0]]))
# print(solution([[1, -1, 0], [2, -1, 0], [4, -1, 0]]))
print(solution([[-1, 1, 0], [1, 1, -4], [1, 1, -2], [1, 1, -8]]))