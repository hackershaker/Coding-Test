def solution(name):
    def change(before, after):
        return min(ord(after) - ord(before), ord(before)-ord("A") + ord("Z")-ord(after) +1)
    
    def findright(list, idx):
        right = 1
        while True:
            if right == len(name): return 21
            if name[(idx+right)%len(name)] == "A" or list[(idx+right)%len(name)] == name[(idx+right)%len(name)]:
                right += 1
            else: break
        return right

    def findleft(list, idx):
        left = -1
        while True:
            if abs(left) == len(name): return -21
            if name[(idx+left+len(name))%len(name)] == "A" or list[(idx+left+len(name))%len(name)] == name[(idx+left+len(name))%len(name)]:
                left -= 1
            else: break
        return left

    initword = [name[0]] + ["A"]*(len(name)-1); idx=0; answer = change("A", name[0])
    name = list(name)
    # print(initword, "idx: ", idx, "answer: ", answer)
    while initword != name:
        left = findleft(initword, idx)
        right = findright(initword, idx)
        # print("left:", left, "right:", right)
        if abs(left) < right:
            idx = (idx + left + len(name))%len(name)
            answer += abs(left) + change(initword[idx], name[idx])
        else:
            idx = (idx + right)%len(name)
            answer += right + change(initword[idx], name[idx])

        initword[idx] = name[idx]
        # print(initword, "idx: ", idx, "answer: ", answer)

    return answer

# print(solution("ABC"), 5)
# print(solution("ZZA"), 3)
# print(solution("CBABC"), 10)
# print(solution("JEROEN"), 56)
# print(solution("AGDEA"), 16)
# print(solution("AAADFX"), 14)
# print(solution("JAN"), 23)
# print(solution("DOG"), 23)
# print(solution("JAZ"), 11)
# print(solution("CAZAA"), 5)
# print(solution("CZAB"), 7)
# print(solution("AAAA"), 0)
# print(solution("BAAB"), 3)
# print(solution("ABAABCA"), 2+4+3)
# print(solution("ABADABCAG"), 21)
# print(solution("ABCAG"), 2+3+8)
# print(solution("EDCBAE"), 4+4+3+2+6)
# print(solution("AAEEAA"), 6+5)
# print(solution("AAEEA"), 6+5)
# print(solution("CBACBA"), 2+2+4+2)
# print(solution("ABZYABCAZAZ"), 2+2+3+3+3+3+3)
# print(solution("ABAAB"), 5)
print(solution("AAIAPB"), 24)
print(solution("DYAOAAAARQANAWA"), 66)
print(solution("ASWAAATDAJAXA"), 45)
print(solution("BADADC"), 1+3+4+5)
print(solution("BADDAC"), 1+3+4+5)
print(solution("BADADAC"), 1+3+4+5)
print(solution("ABADADAC"), 1+3+4+5)
print(solution("AAABBAAAABBAAAAAAA"), 4+2+6+2)
print(solution("AABBBAAAABBAAAABA"), 3+6+2+6+2+2)
# print(solution("ABABAAAAAAABA"), 10)
# print(solution("AZAAAAAAZAZA"), 2+4+3)
# print(solution("AZAAZAAAZAZA"), 2+4+3)