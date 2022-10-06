from itertools import permutations


def solution(numbers):
    answer = 0
    numset = set()

    def isPrime(n):
        if n == 1 or n == 0:
            return False
        if n == 2:
            return True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        else:
            return True

    def sumDigit(n):
        temp = 0
        while n > 0:
            n, r = divmod(n, 10)
            temp += r
        return temp

    for i in range(1, len(numbers) + 1):
        for num in permutations(numbers, i):
            numset.add(int("".join(num)))
    print(numset)
    for n in numset:
        if isPrime(n):
            answer += 1
        # sd = sumDigit(n)
        # if n == 2 or n == 3:
        #     answer += 1
        #     continue
        # elif n % 2 == 0: continue
        # elif n % 5 == 0: continue
        # elif sd % 3 == 0:continue
        # else:
        #     if isPrime(n):
        #         answer += 1

    return answer


# print(solution("17"), 3)
# print(solution("011"), 2)
# print(solution("102"), 1)
# print(solution("1235"), 0)
# print(solution("317"), 5)
# print(solution("017"), 5)
# print(solution("111"), 1)
print(solution("249"), 0)
# print(solution("3334"), 1)
# print(solution("21"), 1)
# print(solution("0"), 0)
# print(solution("1"), 0)
# print(solution("4"), 0)
# print(solution("123000"), 1)
# print(solution("1234567"), 1)
# print(solution("011"), 2)
