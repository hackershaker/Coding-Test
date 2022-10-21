def operation(x: str, st: list) -> None:
    if x == 'top':
        try:
            print(stack[-1])
        except:
            print(-1)
    elif x == "pop":
        try:
            print(st.pop())
        except:
            print(-1)
    elif x == "size":
        print(len(st))
    elif x == "empty":
        print(1) if len(st)==0 else print(0)
    else:
        st.append(int(x.split(" ")[1]))
        
import sys
if __name__=="__main__":
    n = int(input())
    stack = []
    for _ in range(n):
        operation(sys.stdin.readline().strip(), stack)