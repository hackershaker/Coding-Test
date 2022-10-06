def solution(inp):
    a = 0
    while a < int(T):
        inp = input().split(" ")
        inp = list(map(int, inp))
        x1, y1, r1, x2, y2, r2 = inp[0], inp[1], inp[2], inp[3], inp[4], inp[5]

        d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

        if d == r1 + r2:
            print(1)
        elif r1 + d == r2 or r2 + d == r1:
            print(1)
        elif d != 0 and d < r1 + r2:
            print(2)
        elif d == 0 and r1 == r2:
            print(-1)
        else:
            print(0)

        a += 1

    return a


if __name__ == "__main__":
    T = input()
    for _ in range(T):
        print(solution(input()))
