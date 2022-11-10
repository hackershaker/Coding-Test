def solution():
    a, b = map(int, input().split(" "))
    m = a; r = b
    while True:
        m, r = r, m%r
        if r == 0: break
    gcd = m
    lcm = int(a * b / gcd)
    return gcd, lcm

if __name__ == "__main__":
    gcd, lcm = solution()
    print(gcd)
    print(lcm)