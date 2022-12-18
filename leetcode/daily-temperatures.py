# queue에 (index, tempearature) 형식으로 하나씩 저장
# 처음부터 검사, 만약 queue에 들어있는 데이터의 온도가 낮다면
# 이전 일자로부터 온도가 상승한 것이므로 
# (현재 index - 과거 index)가 상승하기까지의 일자가 된다.
# queue의 0번째부터 이 작업을 수행, 만약 queue의 온도가 더 높다면
# queue의 앞에 저장하고 queue의 온도가 더 낮다면
# answer의 값을 갱신하면서 queue의 앞에서부터 하나씩 빼준다.
from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        q = deque([])

        for idx, temp in enumerate(temperatures):
            if not q: q.append((idx, temp))
            else:
                while q:
                    if q[0][1] >= temp:
                        q.appendleft((idx, temp))
                        break
                    else:
                        answer[q[0][0]] = idx - q[0][0]
                        q.popleft()
                if not q: q.append((idx, temp))

        return answer
