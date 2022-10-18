
if __name__=="__main__":
    remainderset = set()
    for _ in range(10):
        inp = input()
        remainderset.add(int(inp)%42)

    print(len(remainderset))
