def solution(a,b):
    print(a+b)

if __name__=="__main__":
    while True:
        try:
            a, b = input().split(" ")
            solution(int(a), int(b))
        except:
            break
    