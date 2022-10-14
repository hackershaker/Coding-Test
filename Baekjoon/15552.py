import sys
def solution(arr):
    print(sum(list(map(int, arr.split(" ")))))

if __name__=="__main__":
    T = int(input())
    for _ in range(T):
        solution(sys.stdin.readline())