def solution():
    return sum(map(lambda x: int(x)**2, input().split(" "))) % 10

if __name__=="__main__":
    answer = solution()
    print(answer)