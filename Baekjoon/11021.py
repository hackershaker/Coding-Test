def solution(n, t):
    print( f"Case #{n}: {sum(t)}")

if __name__=="__main__":
    casenum = int(input())
    case = [] 
    for _ in range(casenum):
        a, b = list(map(int, input().split(" ")))
        case.append((a, b))

    for i in range(len(case)):
        solution(i+1, case[i])