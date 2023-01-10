# 에라토스테네스의 체 이용

def solution():
    nums = {x for x in range(2, 123456*2+1)}

    for i in range(2, 123457):
        for k in range(2*i, 2*123456+1, i):
            nums.discard(k)

    while (n := int(input())) != 0:
        print(len([x for x in nums if n < x <= 2*n]))
        
    return

if __name__=="__main__":
    solution()