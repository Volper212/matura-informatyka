with open('mecz.txt') as file:
    line = file.readline().strip()
    count = 0
    for i in range(1, len(line)):
        if line[i] != line[i - 1]:
            count += 1
    print(count)
