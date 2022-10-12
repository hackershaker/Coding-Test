def solution(n):
    i = 1; result = 1
    while True:
        if result * (i+1) > n: break
        else:
            i += 1
            result *= i
    
    return i