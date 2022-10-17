def solution(a, b):
    print(max(int(a[::-1]), int(b[::-1])))

if __name__=="__main__":
    a, b = input().split()
    solution(a, b)