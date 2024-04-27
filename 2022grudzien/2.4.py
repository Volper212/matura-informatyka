file = open('pary.txt')
lines = file.readlines()
file.close()
for line in lines:
    line = line.strip()
    x, y = map(int, line.split())
    yCopy = y
    while y > x:
        y //= 2
        if x == y:
            print(x, yCopy)
