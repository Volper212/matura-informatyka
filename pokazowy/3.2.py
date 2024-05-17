a = 4
x = 0
M = 10
b = 1

def compute(base, power, modulo):
    if power == 0: return 1
    if power == 1: return base % modulo
    result = compute(base, power // 2, modulo) % modulo
    result = (result * result) % modulo
    if power % 2 == 1:
        result = (result * base) % modulo
    return result


b = compute(a, x, M)
print(b)
