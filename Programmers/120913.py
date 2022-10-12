def solution(my_str, n):
    answer = [my_str[n*i:n*(i+1)] for i in range(int(len(my_str) / n) + 1)]
    return answer

print(solution("abc1Addfggg4556b", 6))