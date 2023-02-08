# 각 node가 연결된 directed graph라고 생각할 수 있고
# bfs를 적용해 최단거리를 구한다.


from collections import defaultdict, deque


class Solution:
    def jump(self, nums: List[int]) -> int:
        dic = defaultdict(int)

        stack = deque([0])
        while stack:
            node = stack.popleft()

            # nums의 길이보다 더 긴 jump를 고려하지 않는다.
            for reach in range(1, min(nums[node] + 1, len(nums) - node)):
                path = dic[node] + 1
                # 최단거리 갱신
                if dic[node + reach] == 0 or path < dic[node + reach]:
                    dic[node + reach] = path
                    # 마지막 노드에 도착하면 bfs 종료
                    if node + reach == len(nums) - 1:
                        break
                    stack.append(node + reach)

        return dic[len(nums) - 1]
