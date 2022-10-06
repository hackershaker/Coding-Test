def solution(n):
    answer = 1; i = 1
    while i <= n:
        if answer % 3 == 0: 
            answer += 1
        elif str(answer).find("3") != -1: 
            answer += 1
        else:
            if i == n and answer % 3 != 0 and str(answer).find("3") == -1: break
            i += 1
            answer += 1
            
        
    return answer

print(solution(8))