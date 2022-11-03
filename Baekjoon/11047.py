def solution(value, k):
    answer = 0
    for x in reversed(value):
        if x > k: continue
        else:
            answer += k // x
            k = k % x

        if k == 0: break
    
    print(answer)
    return answer

if __name__=="__main__":
    n, k = map(int, input().split(" "))
    value = []

    for _ in range(n):
        value.append(int(input()))

    solution(value, k)
    
