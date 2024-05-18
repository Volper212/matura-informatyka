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
with open("trojki.txt", "w") as file:
    for i in range(len(numbers)):
        for next in nexts[i]:
            if len(nexts[next]) > 0:
                count += len(nexts[next])
                for third in nexts[next]:
                    file.write(f"{numbers[i]} {numbers[next]} {numbers[third]}\n")
print(count)
