import sys
def solution():
    n = int(input())
    userList = {j:[] for j in range(1,201)}

    for _ in range(n):
        inp = sys.stdin.readline().strip()
        k = inp.split(" ")
        userList[int(k[0])].append(inp)

    for i in range(1, 201):
        for user in userList[i]:
            print(user)

if __name__=="__main__":
    solution()