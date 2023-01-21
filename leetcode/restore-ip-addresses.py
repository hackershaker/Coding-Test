# 재귀함수를 이용해 ip주소의 4가지 부분 검사

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ipSet = set()

        def recur(sequence:list, string:str):
            print(sequence, string)
            if not string and len(sequence) < 4: return
            if len(sequence) == 3:
                if string and 0 <= int(string) <= 255 and len(string) == len(str(int(string))):
                    ipSet.add(".".join(sequence + [string]))
                return
                
            for i in range(1, 4):
                part, rest = string[:i], string[i:]
                if 0 <= int(part) <= 255 and len(part) == len(str(int(part))):
                    recur(sequence+[part], rest)
                else:
                    break

        recur([], s)
        return ipSet