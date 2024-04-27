file = open('liczby.txt')
lines = file.readlines()
file.close()
numbers = map(int, lines)
numbers = map(hex, numbers)
digits = ''.join([number[2:] for number in numbers])
counts = {}
for digit in '0123456789ABCDEF':
    counts[digit] = 0
for digit in digits:
    counts[digit.upper()] += 1
for digit in counts:
    print(digit, counts[digit], sep=':')
