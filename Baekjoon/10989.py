import sys
def countingSort(): # Counting Sort
    T = int(sys.stdin.readline().strip())
    countList = [0] * 10000
    numlist=[]
    for _ in range(T):
        num = int(sys.stdin.readline().strip())
        numlist.append(num)
        countList[num-1] += 1
    
    for i in range(1, len(countList)):
        countList[i] += countList[i-1]

    answer = [0] * T
    for _ in range(T):
        n = numlist.pop()
        answer[countList[n-1]] = n
        countList[n-1] -= 1

    return answer

import sys
from heapq import heappop, heappush
def heapSort():
    heap = []
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        heappush(heap, int(sys.stdin.readline().strip()))

    # for _ in range(T):
    #     print(heappop(heap))

import sys
def solution():
    T = int(sys.stdin.readline().strip())
    countList = [0] * 10000
    for _ in range(T):
        num = int(sys.stdin.readline().strip())
        countList[num-1] += 1

    i = 0
    while i < len(countList):
        if countList[i] != 0:
            print(i+1)
            countList[i] -= 1
        else:
            i += 1

if __name__=="__main__":
    solution()
