# binary search 이용
# m보다 작은 나무는 들고가면 안 되므로 down 선택


import sys


class Solution():
    def getMaximumHeight(self):
        n, m = map(int, sys.stdin.readline().rstrip().split(" "))
        trees = list(map(int, sys.stdin.readline().rstrip().split(" ")))

        down = 0; up = 1000000000
        while up - down > 1:
            mid = int((down+up)/2)
            cutTree = sum( [0 if mid>=tree else tree-mid for tree in trees ] )
            
            if cutTree == m:
                print(mid)
                return mid
            elif cutTree > m:
                down = mid
            else:
                up = mid

        print(down)
        return down

if __name__=="__main__":
    s = Solution()
    s.getMaximumHeight()