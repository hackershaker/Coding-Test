def solution(begin, end):
    answer = []
    def isPrime(k):
        for i in range(2, int(k**0.5)+1):
            if k%i == 0:
                if int(k/i) <= 10000000:
                    return False, int(k/i)
                else:
                    continue
        return True, 0

    for i in range(begin, end+1):
        isp, maxyak = isPrime(i)
        if not isp:
            answer.append(maxyak)
        elif i == 1:
            answer.append(0)
        else:
            answer.append(1)
        
    return answer

print(solution(1,10), [0, 1, 1, 2, 1, 3, 1, 4, 3, 5])
print(solution(1,20), [0, 1, 1, 2, 1, 3, 1, 4, 3, 5, 1, 6, 1, 7, 5, 8, 1, 9, 1, 10])