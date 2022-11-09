def solution():
    apartment = [[i+1 for i in range(14)]] + [[0 for _ in range(14)] for _ in range(14)]

    for i in range(14):
        for j in range(14):
            if j == 0: apartment[i+1][j] = 1
            else:
                apartment[i+1][j] = apartment[i][j] + apartment[i+1][j-1]
                
    T = int(input())
    for _ in range(T):
        k = int(input())
        n = int(input())
        print(apartment[k][n-1])

if __name__=="__main__":
    solution()
