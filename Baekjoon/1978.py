def isPrime(k):
    if k ==1: return False
    for i in range(2, int(k**0.5)+1):
        if k % i == 0: return False
    return True

if __name__=="__main__":
    T = int(input())
    answer = 0
    for i in map(int, input().split(" ")):
        if isPrime(i): answer += 1
    print(answer)