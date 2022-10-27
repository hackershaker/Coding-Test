def selfNumber(k):
    return k + sum(map(int, str(k)))

if __name__=="__main__":
    numset = {x for x in range(1, 10001)}
    for i in range(1, 10001):
        numset.discard(selfNumber(i))

    for i in sorted(list(numset)):
        print(i)