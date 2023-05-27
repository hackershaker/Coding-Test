import sys
class Solution:
    def solution(self):
        while True:
            string = sys.stdin.readline().strip()
            if string == "0": break

            for i in range(len(string)//2+1):
                if string[i] != string[len(string)-i-1]:
                    sys.stdout.write("no"+"\n")
                    break
            else:
                sys.stdout.write("yes"+"\n")
                


if __name__ == '__main__':
    s = Solution()
    s.solution()