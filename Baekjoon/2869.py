def solution(a,b,v):
    day = (v-a)/(a-b) + 1
    day = -int(-day//1)
    print(day)
    return day

if __name__=="__main__":
    a, b, v = map(int, input().split(" "))
    solution(a,b,v)
    