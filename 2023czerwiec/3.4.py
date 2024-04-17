def contains_zero(string):
    for character in string:
        if character == '0':
            return True
    return False


def sum_different_digits(string):
    different_digits = set()
    for character in string:
        different_digits.add(int(character))
    return sum(different_digits)


with open("anagram.txt") as file:
    numbers = []
    for line in file.readlines():
        numbers.append(int(line, 2))
    strings = [str(number) for number in numbers]
    no_zero_count = len([string for string in strings if not contains_zero(string)])
    print(no_zero_count)
    different_digit_sums = [sum_different_digits(string) for string in strings]
    max_different_digit_sum_index = 0
    for i in range(1, len(different_digit_sums)):
        if different_digit_sums[i] > different_digit_sums[max_different_digit_sum_index]:
            max_different_digit_sum_index = i
    print(strings[max_different_digit_sum_index])
