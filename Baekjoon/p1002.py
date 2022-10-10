def solution(inp):
    answer = 0
    inp = list(map(int, inp.split(" ")))
    x1, y1, r1, x2, y2, r2 = inp[0], inp[1], inp[2], inp[3], inp[4], inp[5]

    d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    if d != 0 and (d == r1 + r2 or r1 + d == r2 or r2 + d == r1):
        answer = 1
    elif d == 0 and r1 != r2 or d + r1 < r2 or d + r2 < r1:
        answer = 0
    elif d != 0 and d < r1 + r2:
        answer = 2
    elif d == 0 and r1 == r2:
        answer = -1
    
    else:
        answer = 0

    return answer



if __name__ == "__main__":
    T = input()
    caselist = []
    for _ in range(int(T)): caselist.append(input())

    for c in caselist: print(solution(c))
