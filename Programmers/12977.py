from itertools import combinations


def solution(nums):
    answer = 0

    def isPrime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        else:
            return True

    for n in combinations(nums, 3):
        if isPrime(sum(n)):
            answer += 1

    return answer


print(solution([1, 2, 3, 4]))
