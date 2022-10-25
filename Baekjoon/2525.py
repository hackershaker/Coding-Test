if __name__=="__main__":
    starth, startm = map(int, input().split(" "))
    cooktime = int(input())

    endm = (cooktime + startm)% 60
    endh = (starth + (cooktime + startm)//60)%24

    print(f"{endh} {endm}")
