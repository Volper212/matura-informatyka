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
for j in range(len(lengths), 3, -1):
    for i in range(j - 1, len(lengths)):
        if lengths[i] >= 0:
            continue
        change = lengths[i]
        if lengths[i + change] == 0 or change == -1:
            change -= 1
        if change <= -(j - 1):
            continue
        if lengths[i + change] - change + 1 < j:
            continue
        print(i - j + 1 + 1)
        for k in range(i - j + 1, i + 1):
            print(digits[k], end="")
        break
    else:
        continue
    break

""" another way (less optimal):
for length in range(len(digits), 3, -1):
    for i in range(len(digits) - (length - 1)):
        j = i
        while j < i + (length - 3) and digits[j] < digits[j + 1]:
            j += 1
        if j > i:
            for k in range(j + 1, i + (length - 1)):
                if not digits[k] > digits[k + 1]:
                    break
            else:
                print(i + 1)
                print("".join([str(digit) for digit in digits[i:i + length]]))
                break
    else:
        continue
    break
"""
