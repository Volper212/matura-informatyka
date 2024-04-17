with open("anagram.txt") as file:
    balanced_count = 0
    almost_balanced_count = 0
    for line in file.readlines():
        zero_count = 0
        one_count = 0
        for character in line.strip():
            if character == '0':
                zero_count += 1
            else:
                one_count += 1
        difference = abs(zero_count - one_count)
        if difference == 0:
            balanced_count += 1
        elif difference == 1:
            almost_balanced_count += 1
    print(balanced_count)
    print(almost_balanced_count)
