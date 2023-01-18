# dp이용
# 끝자리에 주목, 숫자의 끝자리로 분류하면
# 끝자리가 0인 숫자는 1로, 끝자리가 9인 숫자는 8로
# 나머지 숫자는 끝자리가 1 작거나 큰 수로 가므로
# 이를 이용해 계단수를 구한다.


class Solution():

    @classmethod
    def findStairNumber(cls):
        n = int(input())

        dic = {1:[0,1,1,1,1,1,1,1,1,1]}

        for i in range(2, n+1):
            lastDigits = [0] * 10
            for j in range(len(dic[i-1])):
                if j == 0:
                    lastDigits[1] += dic[i-1][0]
                elif j == 9:
                    lastDigits[8] += dic[i-1][9]
                else:
                    lastDigits[j-1] += dic[i-1][j]
                    lastDigits[j+1] += dic[i-1][j]
            dic[i] = lastDigits

        return sum(dic[n]) % 1000000000
                    
if __name__=="__main__":
    answer = Solution.findStairNumber()
    print(answer)