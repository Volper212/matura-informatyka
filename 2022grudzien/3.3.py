N = 1000 * 1000
sito = [True] * (N + 7)
sito[0] = sito[1] = False
primes = []
for i in range(2, N):
    if sito[i]:
        primes.append(i)
        for j in range(i * 2, N, i):
            sito[j] = False
file = open('liczby.txt')
lines = file.readlines()
file.close()
numbers = map(int, lines)
counts = []
for number in numbers:
    count = 0
    for i in range(len(primes)):
        if primes[i] >= number:
            break
        lo = i
        hi = len(primes) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            sum = primes[i] + primes[mid]
            if sum == number:
                count += 1
                break
            if sum < number:
                lo = mid + 1
            else:
                hi = mid - 1
    counts.append((number, count))
largest = counts[0]
smallest = counts[0]
for current in counts:
    if largest[1] < current[1]:
        largest = current
    elif smallest[1] > current[1]:
        smallest = current
print(largest[0], largest[1], smallest[0], smallest[1])
