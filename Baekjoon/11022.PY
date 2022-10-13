def solution(i, c):
    a, b = c
    print(f"Case #{i}: {a} + {b} = {sum(c)}")

if __name__=="__main__":
    T = int(input())
    case = []

    for _ in range(T):
        case.append(list(map(int, input().split(" "))))

    for i, c in enumerate(case):
        solution(i+1, c)