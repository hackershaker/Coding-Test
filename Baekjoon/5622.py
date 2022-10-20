dic = {'ABC':2,'DEF':3,'GHI':4,'JKL':5,"MNO":6,"PQRS":7,"TUV":8,"WXYZ":9}

string = input()
answer = 0

for s in string:
    for key in dic.keys():
        if s in key:
            answer += dic[key] +1

print(answer)
