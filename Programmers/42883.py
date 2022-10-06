def solution2(number, k):
    maxvalue = max(number)

    def getmaxvalue(s):
        temp = []
        for i in range(len(s)):
            temp.append(s[:i] + s[i + 1 :])
        return max(temp)

    delnum = 0
    while delnum < k:
        if number[0] < number[1]:
            number = number[1:]
            delnum += 1
        else:
            maxidx = number.rfind(maxvalue)
            if maxidx == 0:
                number = maxvalue + number[1:].replace(min(number[1:]), "", 1)
                delnum += 1
            elif min(number[:maxidx]) == maxvalue:
                number = (
                    number[:maxidx]
                    + maxvalue
                    + number[maxidx + 1 :].replace(min(number[maxidx + 1 :]), "", 1)
                )
                delnum += 1
            else:
                number = (
                    number[:maxidx].replace(min(number[:maxidx]), "", 1)
                    + number[maxidx:]
                )
                delnum += 1
    return number

from collections import deque
def solution3(number, k): #시간초과
    answer = []; l = len(number); delnum = 0; number = list(number)
    
    while delnum < k:
        deq = deque([])
        for i in range(len(number)):
            deq.append(number[i])
            if len(deq) <= 1:
                continue
            if deq[-1] > deq[-2]:
                del number[i-1]
                delnum += 1
                break
        else:
            minnum = min(number)
            idx = number.index(minnum)
            del number[idx]
            delnum += 1
        
    return ''.join(number)

from collections import deque
def solution(number, k): #시간초과
    windowstart = 0
    deq = deque([])
    delnum = 0
    for i in range(len(number)):
        deq.append(number[i])
        # print(deq, windowstart)
        if len(deq) <= 1 or delnum == k: continue
        else:
            try:
                while delnum < k:
                    for start in range(windowstart, len(deq)):
                        if deq[start] < deq[start+1]:
                            stack = []
                            for _ in range(len(deq) - start -1):
                                stack.append(deq.pop())
                            deq.pop()
                            while stack:
                                deq.append(stack.pop())
                            # print(deq)
                            delnum += 1
                            if delnum == k: break
                            windowstart = start - 1
                            if windowstart < 0: windowstart = 0
                            break
                    else:
                        windowstart += 1
                        break
            except:
                continue
    # print(windowstart)
    
    for _ in range(k - delnum): deq.pop()
        
    return "".join(deq)
    

# print(solution("12", 1), "2")
print(solution("1924", 2), "94")
# print(solution("417658", 3), "768")
print(solution("87965241351", 2), "965241351")
# print(solution("2131234", 3), "3234")
# print(solution("4177252841", 4), "775841")
# print(solution("4177252841", 3), "7752841")
# print(solution("4979283176", 4), "998376")
# print(solution("43212784659", 4), "4784659")
# print(solution("4217658", 1), "427658")
# print(solution("987654321", 2), "9876543")
# print(solution("333222111", 2), "3332221")
# print(solution("123234345456", 4), "34345456")
# print(solution("1239871234321", 6), "9874321")
# print(solution("125425142145", 6), "554245")
print(solution("543219", 2), "5439")
# print(solution("54321987", 3), "54987")
# print(solution("123456789876543212345678987654321", 16), "98765432987654321")
# print(solution("12345678987654321"*58824, 999999), "9876543")
