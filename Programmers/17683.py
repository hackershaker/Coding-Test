import re
def solution(m, musicinfos):
    answer = []
    for info in musicinfos:
        # print(info.split(","))
        starttime, endtime, name, sheet = info.split(",")[0], info.split(",")[1], info.split(",")[2], info.split(",")[3]
        if endtime == "00:00": endtime = "24:00"
        playtime = 0
        if starttime[:2] == endtime[:2]: playtime = int(endtime[3:]) - int(starttime[3:])
        else: playtime = 60 - int(starttime[3:]) + 60 * ( int(endtime[:2]) - int(starttime[:2])-1 ) + int(endtime[3:])
        # print(playtime)
        temp = ""
        while True:
            if len(temp + sheet) > playtime:
                temp += sheet;break
            else: temp += sheet
        sheet = temp
        # print(sheet)
        if re.search(f"{m}[^#]", sheet) != None: answer.append([name, playtime])

    # print(answer)
    if answer: return sorted(answer, key=lambda x: -x[1])[0][0]
    else: return "(None)"


print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]),"HELLO")
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]),"FOO")
print(solution(	"ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]), "WORLD")
print(solution(	"ABC", ["09:58,12:14,HELLO,C#DEFGAB", "22:57,00:00,WORLD,ABCDEF"]), "WORLD")
print(solution(	"ABC", ["16:23,23:50,HELLO,C#DEFGAB", "22:15,23:59,WORLD,ABCDEF"]), "WORLD")
print(solution(	"ABC", ["22:00,23:00,HELLO,CDEFGAB", "22:00,23:00,WORLD,ABCDEF", "22:00,23:00,SSKY,ABCDABCD"]), "HELLO")
print(solution(	"A", ["22:00,23:00,HELLO,CDEFGAB", "22:00,23:00,WORLD,ABCDEF", "22:00,23:00,SSKY,ABCDABCD"]), "HELLO")
print(solution(	"ABC", ["12:00,12:06,HELLO,DEFABC", "12:00,12:06,12:12,WORLD,ABABC#"]), "HELLO")
print(solution(	"F#D#", ["16:23,23:50,HELLO,C#AF#DEF#C#D#", "22:15,23:59,WORLD,F#C#D#A#F#A#D#D#F"]), "(None)")
print(solution(	"CC#C", ["16:23,23:50,HELLO,C#C#CC#", "22:15,23:59,WORLD,C#CC#C#C#"]), "(None)")
print(solution(	"CCC#", ["16:23,23:50,HELLO,CC#C#C", "22:15,23:59,WORLD,C#C#C"]), "HELLO")