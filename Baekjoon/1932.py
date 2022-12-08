def solution():
    n = int(input())
    prevRow = []

    for i in range(n):
        row = list(map(int, input().split(" ")))
        if not prevRow:
            prevRow = row
        else:
            for k in range(len(row)):
                if k == 0:
                    row[k] += prevRow[0]
                elif k == len(row)-1:
                    row[k] += prevRow[-1]
                else:
                    row[k] += max(prevRow[k], prevRow[k-1])
            prevRow = row

    return max(prevRow)

if __name__=="__main__":
    answer = solution()
    print(answer)
