def solution():
    n = int(input())
    if n == 1: return []
    bucket = []
    
    for i in range(2, n+1):
        if n == 1: break
        if n % i == 0:
            while True:
                m, r = divmod(n, i)
                if r == 0:
                    bucket.append(i)
                    n = m
                else: break

    return bucket

def isPrime(a):
    if a == 1: return False
    for i in range(2, -(int(-(a**0.5)//1))):
        if a % i == 0: return False
    return True


if __name__=="__main__":
    answer = solution()
    for ans in answer: print(ans)