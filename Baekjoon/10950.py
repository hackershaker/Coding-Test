def solution(inp):
    a, b = list(map(int, inp.split(" ")))
    print(a + b)


if __name__=="__main__":
    T = int(input())

    for _ in range(T):
        solution(input())