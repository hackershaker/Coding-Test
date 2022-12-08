def solution():
    heights = []
    for _ in range(9):
        x = int(input())
        heights.append(x)
    stack = [[{x}, x] for x in heights]

    while stack:
        h, total = stack.pop()

        if total > 100: continue
        if total == 100 and len(h) == 7:
            return sorted(h)
        for height in heights:
            if height not in h:
                stack.append([h | {height}, total + height])

if __name__=="__main__":
    answer = solution()
    for ans in answer: print(ans) 