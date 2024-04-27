passas = []
with open('mecz.txt') as file:
    line = file.readline().strip()
    passas.append((line[0], 1))
    for i in range(1, len(line)):
        team, length = passas[-1]
        if line[i] == team:
            passas[-1] = team, length + 1
        else:
            if length < 10:
                passas.pop()
            passas.append((line[i], 1))
team, length = passas[-1]
if length < 10:
    passas.pop()
longest = passas[0]
for current in passas:
    if longest[1] < current[1]:
        longest = current
print(len(passas), longest[0], longest[1])
