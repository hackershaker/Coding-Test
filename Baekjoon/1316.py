def solution(s):
    wset = set()
    curalpha = s[0]
    for alphabet in s:
        if alphabet in wset:
            return False
        if alphabet != curalpha:
            wset.add(curalpha)
            curalpha = alphabet
    return True

if __name__=="__main__":
    n = int(input())
    answer = 0
    for _ in range(n):
        if solution(input()): answer += 1
    print(answer)