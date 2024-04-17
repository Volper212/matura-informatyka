digits = ""
with open("pi.txt") as file:
    for line in file.readlines():
        digits += line.strip()
count = 0
for i in range(0, len(digits) - 1):
    if int(digits[i:i + 2]) > 90:
        count += 1
print(count)
