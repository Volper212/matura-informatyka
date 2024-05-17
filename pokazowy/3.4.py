def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


count = 0
with open("liczby.txt") as file:
    for line in file.readlines():
        line = line.strip()
        M = [*map(int, line.split())][0]
        a = [*map(int, line.split())][1]

        if gcd(M, a) == 1:
            count += 1
print(count)
