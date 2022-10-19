def solution(dots):
    dots.sort()
    return int((dots[1][1]-dots[0][1])*(dots[2][0]-dots[0][0]))
