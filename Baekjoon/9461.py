# 6번째 삼각형부터 규칙성: 마지막 삼각형 변 + 5번째 전의 삼각형 변 = 다음 삼각형 변

def solution():
    lines = [1, 1, 1, 2, 2, 3]
    T = int(input())

    for _ in range(T):
        n = int(input())
        while len(lines) < n:
            lines.append(lines[-1] + lines[-5])

        print(lines[n-1])

if __name__=="__main__":
    solution()