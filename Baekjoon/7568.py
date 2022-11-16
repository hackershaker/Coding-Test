def solution():
    T = int(input())
    grade = []
    for i in range(T):
        x = input().split(" ")
        grade.append([int(x[0]), int(x[1]), i, 1])

    compareArray = [[0 for _ in range(T)] for _ in range(T)]
    for i in range(T):
        for j in range(T):
            if i == j: continue
            if grade[i][0] < grade[j][0] and grade[i][1] < grade[j][1]:
                compareArray[i][j] = 1
    
    result = [sum(x)+1 for x in compareArray]
    print(" ".join(map(str, result)))
    return result

if __name__=="__main__":
    solution()