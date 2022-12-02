def solution():
    month, day = map(int, input().split(" "))
    mdlist = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31,]

    totalDay = 0
    for i in range(1, month):
        totalDay += mdlist[i-1]
    
    totalDay += day

    today = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN', ]
    return today[(totalDay-1) % 7]

if __name__=="__main__":
    answer = solution()
    print(answer)