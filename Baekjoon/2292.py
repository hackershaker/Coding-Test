def getfloor(k):
    i = 1
    num = 1
    while k > num:
        i += 1
        num += i*6 -6
    return i

def solution(k):
    print(getfloor(k))
    return getfloor(k)

if __name__ == "__main__":
    solution(int(input()))