def solution():
    n = int(input())
    return "".join( sorted(str(n), reverse=True) )

if __name__=="__main__":
    answer = solution()
    print(answer)