def format_fragment(index):
    if index < 10:
        return f'0{index}'
    return str(index)


occurrence_counts = [0] * 100
digits = ""
with open("pi.txt") as file:
    for line in file.readlines():
        digits += line.strip()
for i in range(0, len(digits) - 1):
    occurrence_counts[int(digits[i:i + 2])] += 1
max_index = 0
min_index = 0
for i in range(1, len(occurrence_counts)):
    if occurrence_counts[max_index] < occurrence_counts[i]:
        max_index = i
    elif occurrence_counts[min_index] > occurrence_counts[i]:
        min_index = i
print(format_fragment(min_index), occurrence_counts[min_index])
print(format_fragment(max_index), occurrence_counts[max_index])
