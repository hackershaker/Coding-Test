def solution():
    n = input()
    numSet = set(input().split(" "))

    m = input()
    for number in input().split(" "):
        if number in numSet: print(1)
        else: print(0)

if __name__=="__main__":
    solution()