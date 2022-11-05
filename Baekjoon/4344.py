def solution(n, students):
    avg = sum(students) / len(students)
    k = [ x for x in students if x > avg ]
    print("%.3f" % (len(k)/len(students) * 100) + "%")


if __name__=="__main__":
    T = int(input())
    
    for _ in range(T):
        caselist = list(map(int, input().split(" ")))
        solution(caselist[0], caselist[1:])