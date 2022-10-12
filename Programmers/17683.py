import re
def solution2(m, musicinfos):
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
        lensheet = len(sheet) - sheet.count("#")
        for _ in range(int(playtime/lensheet)): temp += sheet
        c = 0; i=0
        while c < playtime % lensheet:
            try:
                if sheet[i].isalpha() and sheet[i+1] == "#": 
                    temp += sheet[i:i+2]
                    c += 1
                    i += 1
                else:
                    temp += sheet[i]
                    c += 1
                    i += 1
            except:
                temp += sheet[i]
                c += 1

        sheet = temp
        # print(sheet)

        if re.search(f"{m}[A-Z]", sheet) != None:
            # print("Gotcha")
            answer.append([name, playtime])
        else:
            if re.search(f"{m}$", sheet) != None:
                answer.append([name, playtime])

    # print(answer)
    if answer: return sorted(answer, key=lambda x: -x[1])[0][0]
    else: return "(None)"

from collections import deque
def solution(m, musicinfos):
    answer = []
    for info in musicinfos:
        starttime, endtime, name, sheet = info.split(",")[0], info.split(",")[1], info.split(",")[2], info.split(",")[3]
        playtime = 0
        if starttime[:2] == endtime[:2]: playtime = int(endtime[3:]) - int(starttime[3:])
        else: playtime = 60 - int(starttime[3:]) + 60 * ( int(endtime[:2]) - int(starttime[:2])-1 ) + int(endtime[3:])
        # print(playtime)
        
        melody = []; sheet = deque(sheet)
        while True:
            try:
                note = sheet.popleft()
                if note == "#":
                    prevnote = melody.pop()
                    melody.append(prevnote + note)
                else:
                    melody.append(note)
            except: break

        melody = melody * (playtime // len(melody)) + melody[:playtime % len(melody)]
        # print(m, melody)

        # if len(melody) < len(m): continue
        deq = deque(melody[:len(m) - m.count("#")])
        # print(deq)
        i = len(m) - m.count("#")
        while True:
            # print(deq, m)
            try:
                if ''.join(deq) == m:
                    answer.append([name, playtime])
                    break
                else:
                    deq.popleft()
                    deq.append(melody[i])
                    i += 1
            except:
                break
    # print(answer)
    if len(answer) == 0: return "(None)"
    else: return sorted(answer, key=lambda x: (-x[1]))[0][0]



# print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]),"HELLO")
# print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]),"FOO")
# print(solution(	"ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]), "WORLD")
# print(solution(	"ABC", ["09:58,12:14,HELLO,C#DEFGAB", "22:57,00:00,WORLD,ABCDEF"]), "WORLD")
# print(solution(	"ABC", ["16:23,23:50,HELLO,C#DEFGAB", "22:15,23:59,WORLD,ABCDEF"]), "WORLD")
# print(solution(	"ABC", ["22:00,23:00,HELLO,CDEFGAB", "22:00,23:00,WORLD,ABCDEF", "22:00,23:00,SSKY,ABCDABCD"]), "HELLO")
# print(solution(	"A", ["22:00,23:00,HELLO,CDEFGAB", "22:00,23:00,WORLD,ABCDEF", "22:00,23:00,SSKY,ABCDABCD"]), "HELLO")
# print(solution(	"ABC", ["12:00,12:06,HELLO,DEFABC", "12:00,12:06,12:12,WORLD,ABABC#"]), "HELLO")
# print(solution(	"F#D#", ["16:23,23:50,HELLO,C#AF#DEF#C#D#", "22:15,23:59,WORLD,F#C#D#A#F#A#D#D#F"]), "(None)")
# print(solution(	"CC#C", ["16:23,23:50,HELLO,C#C#CC#", "22:15,23:59,WORLD,C#CC#C#C#"]), "(None)")
# print(solution(	"CCC#", ["00:50,23:50,HELLO,CC#C#C", "12:15,23:01,WORLD,C#C#C"]), "HELLO")
# print(solution(	"CC#", ["16:23,16:24,HELLO,C#C#C#", "22:15,23:59,WORLD,CCC"]), "(None)")
# print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:02,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]),"(None)")
# print(solution(	"ABC", ["20:00,23:00,HELLO,CDEFGAB", "19:00,23:00,WORLD,ABCDEF", "18:00,23:00,SSKY,ABCDABCD"]), "SSKY")
# print(solution(	"ABC", ["20:00,23:00,HELLO,CDEFGAB", "19:00,20:00,WORLD,ABCDEF", "18:00,19:00,SSKY,ABCDABCD"]), "HELLO")
# print(solution(	"ABC", ["09:50,09:58,HELLO,C#DEFGAB", "09:50,09:53,WORLD,ABCDEF#"]), "WORLD")
# print(solution("EF#G#A#", ["09:50,09:56,WORLD,G#A#EF#", "09:50,09:54,GEUST,A#AAAAA#"]), "WORLD")