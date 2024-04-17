digits = []
with open("pi.txt") as file:
    for line in file.readlines():
        digits.append(int(line.strip()))
count = 0
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
