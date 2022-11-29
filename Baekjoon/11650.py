import sys
def solution():
    n = int(input())
    points = []
    for _ in range(n):
        points.append(list(map(int, sys.stdin.readline().strip().split(" "))))

    points = sorted(points, key=lambda x: (x[0], x[1]))

    for point in points:
        print(" ".join(map(str, point)))

if __name__=="__main__":
    solution()