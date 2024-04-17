def contains_zero(string):
    for character in string:
        if character == '0':
            return True
    return False


with open("anagram.txt") as file:
    numbers = []
    for line in file.readlines():
        numbers.append(int(line, 2))
    largest_difference = 0
    for i in range(1, len(numbers)):
        largest_difference = max(largest_difference, abs(numbers[i] - numbers[i - 1]))
    print(bin(largest_difference)[2:])
