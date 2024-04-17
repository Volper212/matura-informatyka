count = 0
with open("bin.txt") as file:
    for line in file.readlines():
        line = line.strip()
        number = int(line, 2)
        block_count = 1
        last_digit = number % 2
        number = number // 2
        while number > 0:
            digit = number % 2
            if digit != last_digit:
                block_count += 1
            last_digit = digit
            number = number // 2

        count += block_count <= 2
print(count)
