def solution():
    k = int(input())
    floor = (2*k + 0.25)**0.5 - 0.5
    if int(floor) == floor:
        floor = int(floor)-1
    else:
        floor = int(floor)

    if (floor+1) % 2 == 1:
        q = k - int((floor+1)*(floor)/2)
        p = floor + 2 - q
    else:
        p = k - int((floor+1)*(floor)/2)
        q = floor + 2 - p
    
    return str(p) + "/" + str(q)

if __name__=="__main__":
    answer = solution()
    print(answer)