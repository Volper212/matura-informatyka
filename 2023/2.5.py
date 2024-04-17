with open("bin.txt") as file:
    with open("wyniki2_5.txt", "w") as results:
        for line in file.readlines():
            line = line.strip()
            number = int(line, 2)
            result = bin(number ^ (number // 2))[2:]
            print(result)
            results.write(result + '\n')
