# dictionary를 이용한 deque 구축
# 빠른 입출력을 위해 sys모듈 사용
# sys.stdout.readline을 쓸 때 개행문자 처리 주의


import sys


class Queue:
    def __init__(self) -> None:
        self.array = {}
        self.start = 0
        self.end = -1

    def pushFront(self, x):
        self.start -= 1
        self.array[self.start] = x

    def pushBack(self, x):
        self.end += 1
        self.array[self.end] = x

    def popFront(self):
        if self.empty() == "0":
            sys.stdout.write(self.array.pop(self.start)+"\n")
            self.start += 1
        else: sys.stdout.write("-1\n")

    def popBack(self):
        if self.empty() == "0":
            sys.stdout.write(self.array.pop(self.end)+"\n")  
            self.end -= 1
        else: sys.stdout.write("-1\n")

    def size(self):
        sys.stdout.write(str(len(self.array))+"\n")

    def empty(self):
        return "1" if self.start > self.end else "0"

    def front(self):
        sys.stdout.write(self.array[self.start]+"\n") if self.empty() == "0" else sys.stdout.write("-1\n")

    def back(self):
        sys.stdout.write(self.array[self.end]+"\n") if self.empty() == "0" else sys.stdout.write("-1\n")

    def orderProcessing(self):
        n = int(sys.stdin.readline())

        for _ in range(n):
            order = sys.stdin.readline().rstrip().split(" ")

            if order[0] == "push_front":
                self.pushFront(order[1])
            elif order[0] == "push_back":
                self.pushBack(order[1])
            elif order[0] == "pop_front":
                self.popFront()
            elif order[0] == "pop_back":
                self.popBack()
            elif order[0] == "size":
                self.size()
            elif order[0] == "empty":
                sys.stdout.write(self.empty()+"\n")
            elif order[0] == "front":
                self.front()
            else:
                self.back()

def solution():
    q = Queue()
    q.orderProcessing()

if __name__=="__main__":
    q = Queue()
    q.orderProcessing()