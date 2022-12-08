def solution():
    line = input()
    i = 0
    while i < len(line):
        print(line[i:i+10])
        i += 10

if __name__=="__main__":
    solution()
