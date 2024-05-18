numbers = []
with open("liczby.txt") as file:
    for line in file.readlines():
        line = line.strip()
        number = int(line)
        numbers.append(number)
numbers.sort()
nexts = [[] for number in numbers]
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[j] % numbers[i] == 0:
            nexts[i].append(j)
count = 0
for i in range(len(numbers)):
    for second in nexts[i]:
        for third in nexts[second]:
            for fourth in nexts[third]:
                count += len(nexts[fourth])
print(count)
