digits = []
with open("pi.txt") as file:
    for line in file.readlines():
        digits.append(int(line.strip()))
lengths = [0]
for i in range(1, len(digits)):
    if digits[i] > digits[i - 1]:
        lengths.append(max(1, lengths[i - 1] + 1))
    elif digits[i] < digits[i - 1]:
        lengths.append(min(-1, lengths[i - 1] - 1))
    else:
        lengths.append(0)
count = 0
for i in range(5, len(lengths)):
    if lengths[i] >= 0:
        continue
    change = lengths[i]
    if lengths[i + change] == 0 or change == -1:
        change -= 1
    if change <= -5:
        continue
    if lengths[i + change] - change + 1 < 6:
        continue
    count += 1
print(count)

""" another way:
count = 0
for i in range(len(digits) - 5):
    j = i
    while j < i + 3 and digits[j] < digits[j + 1]:
        j += 1
    if j > i:
        for k in range(j + 1, i + 5):
            if not digits[k] > digits[k + 1]:
                break
        else:
            count += 1
print(count)
"""