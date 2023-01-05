# points를 시작점으로 sort하여 iteration
# commonInterval : 현재 화살이 관통하는 공통 구간
# 처음 공통구간은 point로 설정
# 다음 point와 공통구간이 있는지 검사
# 공통구간의 끝이 point의 시작보다 크면 공통구간이 있다는 것이므로
# 화살이 같이 관통할 수 있다.
# 공통구간을 [max(commonInterval[0], point[0]), min(commonInterval[1], point[1])] 로 초기화해주어야 한다.
# 만약 공통구간의 끝보다 point의 시작점이 크면 공통구간이 없다는 것이므로 
# commonInterval을 새로운 point로 설정
# 이때 arrow값에 +1 한다
# 최후의 arrow 값 return


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        arrow = 0
        
        commonInterval = [float("inf"), float("-inf")]

        for point in points:
            if point[0] <= commonInterval[1]  :
                commonInterval = [max(commonInterval[0], point[0]), min(commonInterval[1], point[1])]
            else:
                commonInterval = point
                arrow += 1

        return arrow