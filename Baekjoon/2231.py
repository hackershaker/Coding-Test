def solution():
    k = int(input())
    for i in range(1, k):
        if sum(map(int, str(i))) + i == k:
            return i
    return 0

if __name__=="__main__":
    answer = solution()
    print(answer)