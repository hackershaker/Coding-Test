def solution(lines):
    maxIdx = lines.index(max(lines))

    return "right" if lines[maxIdx]**2 == lines[(maxIdx+1)%3]**2 + lines[(maxIdx+2)%3]**2 else "wrong"

if __name__=="__main__":
    while True:
        lines = list(map(int, input().split(" ")))
        if lines == [0,0,0]: break
        answer = solution(lines)
        print(answer)
    