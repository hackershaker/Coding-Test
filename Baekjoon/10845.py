import sys
class Queue:
    def __init__(self) -> None:
        self.length = 0
        self.start = 0
        self.end = -1
        self.dic={}

    def push(self, x):
        self.end += 1
        self.length += 1
        self.dic[self.end] = x
        return

    def pop(self):
        if self.length == 0: return -1
        else: 
            self.start += 1
            self.length -= 1
            return self.dic.pop(self.start - 1)

    def size(self):
        return self.length

    def empty(self):
        return 0 if self.length else 1

    def front(self):
        return self.dic[self.start] if self.length else -1
    
    def back(self):
        return self.dic[self.end] if self.length else -1

def solution():
    q = Queue()
    n = int(input())
    
    for _ in range(n):
        command = sys.stdin.readline().strip()
        if command == "pop": print(q.pop())
        elif command == "size": print(q.size())
        elif command == "empty": print(q.empty())
        elif command == "front": print(q.front())
        elif command == "back": print(q.back())
        else:
            q.push(command.split(" ")[1])
        # print(q.dic, q.start, q.end, q.length)

if __name__=="__main__":
    solution()