def isvps(string):
    stack = []

    for s in string:
        if len(stack)==0:
            stack.append(s)
            continue
        if stack[-1] == "(" and s == ")":
            stack.pop()
        else:
            stack.append(s)

    return "NO" if len(stack) else "YES"

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        print(isvps(input()))