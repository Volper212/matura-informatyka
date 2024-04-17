digits = []
with open("pi.txt") as file:
    for line in file.readlines():
        digits.append(int(line.strip()))
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
