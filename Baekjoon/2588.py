a = int(input())
b = int(input())

print(a * (b%10))
print(a * int((b%100 - b%10)/10))
print(a * int((b%1000 - b%100)/100))
print(a* b)
