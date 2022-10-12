hour, minute = list(map(int, input().split(" ")))

if minute >= 45: print(str(hour) + " " + str(minute-45))
else: print(str((hour - 1 + 24)%24) + " " + str(60 - (45-minute)))