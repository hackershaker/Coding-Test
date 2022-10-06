from functools import reduce
import operator


def solution(numbers):
    return reduce(operator.add, range(1, 10)) - sum(numbers)


print(solution([1, 2, 3, 4, 6, 7, 8, 0]))
print(solution([5, 8, 4, 0, 6, 7, 9]))
