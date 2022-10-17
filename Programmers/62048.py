import math
def solution2(w,h):
    def getsquare(w,h):
        temp = 0
        gi = max(w,h) / min(w,h)
        l = [0]
        for i in range(1, w+1):
            try:
                temp += -(-l[i]//1) - int(l[i-1])
            except:
                l.append(gi * i)
                temp += -(-l[i]//1) - int(l[i-1])
            # print(temp)
        return int(temp)

    gcd = math.gcd(w,h)

    unusedsquare = getsquare(int(w/gcd), int(h/gcd)) * gcd

    return w * h - unusedsquare

import math
def solution3(w, h):
    if w == h:
        return int(w*(w-1))
    gcd = math.gcd(w,h)
    temp = 0
    gi = h / w
    for i in range(1, int(w/gcd)):
        temp += int(gi * i) * 2
    temp = temp * gcd + (gcd-1)*w*h/(2*gcd) * 2
    return int(temp)

import math
def solution4(w, h):
    answer = 0
    gi = h / w
    if w == h:
        return int(w*(w-1))
    gcd = math.gcd(w,h)
    if gcd == 1:
        for i in range(1, w):
            answer += int(gi * i)
        return answer
    else:
        temp = 0
        for i in range(1, int(w/gcd)):
            temp += int(gi * i) * 2
        temp = temp * gcd + (gcd-1)*w*h/(2*gcd) * 2
        return int(temp)

import math
def solution(w, h):
    gcd = math.gcd(w, h)
    answer = 0
    if w < h:
        gi = h / w
        for i in range(1, int(w/gcd)):
            answer += int(gi * i)
        return answer*gcd*2 + int((gcd-1)/gcd * h * w /2) * 2
    elif w == h:
        return int(w*(w-1))
    else:
        gi = w / h
        for i in range(1, int(h/gcd)):
            answer += int(gi * i)
        return answer*gcd*2 + int((gcd-1)/gcd * h * w /2) * 2
    
print(solution(	8, 12 ), 80)
print(solution(	2, 3 ), 2)
print(solution(	3, 2 ), 2)
print(solution(	3, 3 ), 6)
print(solution(	3, 4 ), 6)
print(solution(	3, 5 ), 8)
print(solution(	3, 7 ), 12)
print(solution(	3, 8 ), 14)
print(solution(	1, 5 ), 0)
print(solution(	1, 1 ), 0)
print(solution(	2, 10 ), 10)
print(solution(	4, 9 ), 24)
print(solution(	100000000, 100000000 ), 24)
# print(solution(	100000000, 99999999 ), 24)
