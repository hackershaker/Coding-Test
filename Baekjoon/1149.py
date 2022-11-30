from pprint import pprint
def solution():
    n = int(input())
    answer = [[0, 0, 0]]
    for i in range(n):
        house = list(map(int, input().split(" ")))
        temp = answer[-1]
        answer.append([house[0]+min(temp[1], temp[2]), house[1]+min(temp[2], temp[0]), house[2]+min(temp[0], temp[1])])

    return min(answer[-1])

if __name__ == "__main__":
    answer = solution()
    print(answer)
