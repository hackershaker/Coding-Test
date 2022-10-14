def solution(arr):
    print(max(arr))
    print(arr.index(max(arr)) + 1)

if __name__=="__main__":
    case = []
    while True:
        try:    
            case.append(int(input()))
        except:
            solution(case)
            break
