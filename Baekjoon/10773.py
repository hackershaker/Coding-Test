def solution():
    k = int(input())
    stack = []; total = 0

    for _ in range(k):
        n = int(input())
        if n == 0:
            wrong = stack.pop()
            total -= wrong
        else:
            stack.append(n)
            total += n

    return total

if __name__=="__main__":
    answer = solution()
    print(answer)

