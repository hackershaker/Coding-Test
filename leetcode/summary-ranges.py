class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        answer = []
        if not nums:
            return answer
        start, end = "", ""
        for num in nums:
            if not start:
                start, end = str(num), str(num)
            elif int(end) + 1 < num:
                if start == end:
                    answer.append(start)
                else:
                    answer.append(start + "->" + end)
                start, end = str(num), str(num)
            else:
                end = str(num)
        else:
            if start == end:
                answer.append(start)
            else:
                answer.append(start + "->" + end)

        return answer
