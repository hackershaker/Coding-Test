
# Dynamic Programming
# 2xn 크기의 타일은 2x(n-1)타일에 2×1타일 1개를 추가한 경우의 수에
# 2x(n-2)타일에 1x2타일 1개를 추가한 경우의 수의 합과 같다.
# 추가한다는 것은 맨 앞에 붙인다는 것.
# 맨 앞에 추가하는 타일이 서로 다르므로 겹치는 경우가 없다고 보장할 수 있다.
# 메모이제이션으로 구한 값 저장한 후 해당 n값에 해당하는 value 리턴



def solution():
    n = int(input())
    dic = {1:1, 2:2}

    for i in range(3, n+1):
        dic[i] = dic[i-1] + dic[i-2]

    return dic[n]

if __name__=="__main__":
    answer = solution()
    print(answer%10007)