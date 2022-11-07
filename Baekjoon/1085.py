def solution(x, y, w, h):
    return min(x, y, w-x, h-y)

if __name__=="__main__":
    x,y,w,h = map(int, input().split(" "))
    print(solution(x,y,w,h))
