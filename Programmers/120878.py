from math import gcd
def solution(a, b):
    b = int(b/gcd(a,b)); answer = 0

    while True:
        if b == 1: 
            answer = 1
            break
        if b % 2 == 0: b = int(b/2)
        elif b % 5 == 0: b = int(b/5)
        else:
            answer = 2
            break

    return answer
            
