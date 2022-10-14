def solution(arr):
    maxvalue = max(arr)
    return sum(arr) / len(arr) * 100 / maxvalue

if __name__=="__main__":
    T = int(input())
    case = list(map(int, input().split(" ")))

    print(solution(case))