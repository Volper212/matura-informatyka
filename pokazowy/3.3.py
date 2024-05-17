prime = [True] * 10007
prime[0] = prime[1] = False
for i in range(2, 10003):
    if prime[i]:
        for j in range(i * 2, 10003, i):
            prime[j] = False

count = 0
with open("liczby.txt") as file:
    for line in file.readlines():
        line = line.strip()
        M = [*map(int, line.split())][0]
        if prime[M]:
            count += 1
print(count)
