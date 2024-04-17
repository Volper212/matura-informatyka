n = int("1110101011001", 2)

b = 1
last_digit = n % 2
n = n // 2
while n > 0:
    digit = n % 2
    if digit != last_digit:
        b += 1
    last_digit = digit
    n = n // 2

print(b)
