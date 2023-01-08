# 기울기, 절편을 key로 하는 angle에 point들을 저장
# 기울기가 무한대가 될 경우는 예외처리로 저장
# angle의 value들 중 길이가 가장 긴 원소의 길이를 return


from collections import defaultdict


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        angle = defaultdict(set)

        for i in range(len(points)):
            for j in range(i+1, len(points)):
                a, b = points[i], points[j]
                try:
                    angle[((a[1]-b[1])/(a[0]-b[0]), (b[0]*a[1] - a[0]*b[1])/(b[0]-a[0]))].update([tuple(points[i]), tuple(points[j])])
                except:
                    angle[("inf", a[0])].update([tuple(points[i]), tuple(points[j])])

        return len(max(angle.values(), key=len))

        
