def solution():
    rooms = []
    for i in range(n := int(input())):
        rooms.append(list(map(int, input().split(" "))))

    rooms.sort(key=lambda x: (x[1], x[0]))
    timeTable = []

    for meeting in rooms:
        try:
            if timeTable[-1][1] <= meeting[0]:
                timeTable.append(meeting)
        except:
            timeTable.append(meeting)

    return len(timeTable) 

if __name__=="__main__":
    answer = solution()
    print(answer)