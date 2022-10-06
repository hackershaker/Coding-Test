import math
def solution(rows, columns, queries):
    answer = []
    array = [[0]*columns for _ in range(rows)]
    element = 1
    for k in range(rows):
        for j in range(columns):
            array[k][j] = element; element += 1
    # print(array)

    # 회전 구현
    for q in queries:
        startpoint = [q[0], q[1]]; minnum = []; startvalue = array[q[0]-1][q[1]-1]; prevvalue = startvalue
        for i in range(q[1]+1, q[3]+1):
            print(f"move {(q[0]-1, i-2)} to {(q[0]-1, i-1)}")
            temp = array[q[0]-1][i-1]
            minnum.append(temp)
            array[q[0]-1][i-1] = prevvalue
            prevvalue = temp
        print(array)
        for i in range(q[0]+1, q[2]+1):
            print(f"move {(i-2, q[3]-1)} to {(i-1, q[3]-1)}")
            temp = array[i-1][q[3]-1]
            minnum.append(temp)
            array[i-1][q[3]-1] = prevvalue
            prevvalue = temp
        print(array)
        for i in range(q[3], q[1], -1):
            print(f"move {(q[2]-1, i-1)} to {(q[2]-1, i-2)}")
            temp = array[q[2]-1][i-2]
            minnum.append(temp)
            array[q[2]-1][i-2] = prevvalue
            prevvalue = temp
        print(array)
        for i in range(q[2], q[0], -1):
            print(f"move {(i-1, q[1]-1)} to {(i-2, q[1]-1)}")
            temp = array[i-2][q[1]-1]
            minnum.append(temp)
            array[i-2][q[1]-1] = prevvalue
            prevvalue = temp
        print(array)
        answer.append(min(minnum))
    return answer

# print(solution(6, 6, [[2, 2, 5, 4]]))
print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))