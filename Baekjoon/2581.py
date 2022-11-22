def solution():
    m = int(input())
    n = int(input())

    nums = {i+1 for i in range(n)}
    nums.discard(1)

    for k in range(2, int(n/2)+1):
        if k not in nums: continue
        i = 2
        while i*k <= n:
            nums.discard(i*k)
            i += 1
    # print(nums)
    nums = [x for x in nums if x >= m]
    if len(nums) == 0: return -1
    
    s = sum(nums)
    minNum = min(nums)
    return (s, minNum)

if __name__=="__main__":
    answer = solution()
    if type(answer) == tuple:
        print(answer[0])
        print(answer[1])
    else:
        print(answer)
