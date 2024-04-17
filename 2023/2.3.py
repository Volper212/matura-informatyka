largest = 0
with open("bin.txt") as file:
    for line in file.readlines():
        line = line.strip()
        number = int(line, 2)
        if number > largest:
            largest = number
print(bin(largest)[2:])