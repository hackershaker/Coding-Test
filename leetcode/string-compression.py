class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        target = None
        consecutive = 0
        for char in chars:
            if not target:
                target = char
                consecutive += 1
            elif target == char:
                consecutive += 1
            else:
                s += target
                if consecutive > 1:
                    s += str(consecutive)
                target = char
                consecutive = 1
        else:
            s += target
            if consecutive > 1:
                s += str(consecutive)
        for i in range(len(s)):
            chars[i] = s[i]
        return len(s)
