count = 0
first = 0
with open("liczby.txt") as file:
    for line in file.readlines():
        line = line.strip()
        if line[0] == line[-1]:
            if count == 0:
                first = int(line)
            count += 1
print(count, first)
