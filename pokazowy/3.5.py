def compute(base, power, modulo):
    if power == 0: return 1
    if power == 1: return base % modulo
    result = compute(base, power // 2, modulo) % modulo
    result = (result * result) % modulo
    if power % 2 == 1:
        result = (result * base) % modulo
    return result


count = 0
with open("liczby.txt") as file:
    for line in file.readlines():
        line = line.strip()
        M = [*map(int, line.split())][0]
        a = [*map(int, line.split())][1]
        b = [*map(int, line.split())][2]

        for x in range(0, M):
            if compute(a, x, M) == b:
                count += 1
                break
print(count)