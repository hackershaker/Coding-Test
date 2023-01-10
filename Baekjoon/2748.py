# dp이용

def solution():
    n = int(input())
    fibonacci = [1,1,2]

    while len(fibonacci) < n:
        fibonacci.append(fibonacci[-1]+fibonacci[-2])

    return fibonacci[n-1]

if __name__=="__main__":
    answer = solution()
    print(answer)