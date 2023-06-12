import sys


class Solution:
    def solution(self):
        students = 30
        notSubmit = 2
        attendance = 2**students - 1
        for _ in range(students - notSubmit):
            n = int(sys.stdin.readline().strip())
            attendance = attendance & ~(2 ** (n - 1))

        answer = []
        i = 1
        while attendance:
            if attendance & 1 == 1:
                answer.append(i)
            attendance = attendance >> 1
            i += 1
        
        for a in answer:
            print(a)


if __name__ == "__main__":
    s = Solution()
    s.solution()
