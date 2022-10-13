def solution(numbers):
    a, b, c = numbers
    result = a*b*c

    for i in range(10):
        print(str(result).count(str(i)))

if __name__ == "__main__":
    number = []
    for _ in range(3): number.append(int(input()))
    solution(number)