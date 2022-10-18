def factorial(k):
    if k == 0 or k == 1: return 1
    n = 2
    while True:
        list.append(list[-1]*n)
        if n == k: return list[k]
        n += 1

if __name__=="__main__":
    list=[1, 1]
    n = int(input())
    print(factorial(n))