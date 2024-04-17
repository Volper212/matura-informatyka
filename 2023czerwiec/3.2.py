with open("anagram.txt") as file:
    for line in file.readlines():
        line = line.strip()
        if len(line) == 8:
            zero_count = 0
            one_count = 0
            for character in line:
                if character == '0':
                    zero_count += 1
                else:
                    one_count += 1
            if one_count - zero_count == 0 or one_count - zero_count == 2:
                print(line)
