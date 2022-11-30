def solution():
    total = 0
    while True:
        try:
            if (k := int(input())) < 40: total += 40
            else: total += k
        except:
            return int(total / 5)

if __name__=="__main__":
    answer = solution()
    print(answer)