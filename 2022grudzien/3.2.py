N = 1000 * 1000
sito = [True] * (N + 7)
sito[0] = sito[1] = False
for i in range(2, N):
    if sito[i]:
        for j in range(i * 2, N, i):
            sito[j] = False
file = open('liczby.txt')
lines = file.readlines()
file.close()
numbers = map(int, lines)
count = 0
for number in numbers:
    if sito[number - 1]:
        count += 1
print(count)
