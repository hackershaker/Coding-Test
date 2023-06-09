class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if ord(letters[-1]) <= ord(target):
            return letters[0]
        start, end = 0, len(letters) - 1
        while start < end:
            mid = (start + end) // 2
            if ord(letters[mid]) > ord(target):
                end = mid
            else:
                start = mid + 1
        return letters[end]
