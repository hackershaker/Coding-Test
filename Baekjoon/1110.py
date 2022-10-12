def solution(N):
    N = int(N)
    target = N
    cycles = 0; stack = [N]
    # print(N)
    while True:
        convnum = stack.pop()
        # print(convnum, "=======>")
        if convnum < 10: convnum = (convnum%10)*10 + int(str(convnum % 10 + convnum // 10)[-1])
        else: convnum = (convnum % 10) * 10 + int(str(convnum % 10 + convnum // 10)[-1])
        # print(convnum)
        stack.append(convnum)
        cycles += 1
        
        if stack[-1] == target: break

    print(cycles)
    return str(cycles)


if __name__ == "__main__":
    N = int(input())
    solution(N)