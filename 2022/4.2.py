prime = [True] * (100 * 1000 + 7)
prime[0] = prime[1] = False
primes = []
for i in range(2, 100 * 1000 + 3):
    if not prime[i]:
        continue
    for j in range(i * i, 100 * 1000 + 3, i):
        prime[j] = False
    primes.append(i)


def find_factors(number):
    for prime in primes:
        if number % prime == 0:
            return [prime, *find_factors(number // prime)]
    return []


def find_factor_count(number):
    return len(find_factors(number))


def find_different_factor_count(number):
    return len(set(find_factors(number)))


biggest = 0, 0
biggest_different = 0, 0
with open("liczby.txt") as file:
    for line in file.readlines():
        line = line.strip()
        number = int(line)
        factor_count = find_factor_count(number)
        different_factor_count = find_different_factor_count(number)
        if biggest[1] < factor_count:
            biggest = number, factor_count
        if biggest_different[1] < different_factor_count:
            biggest_different = number, different_factor_count
print(biggest[0], biggest[1], biggest_different[0], biggest_different[1])
