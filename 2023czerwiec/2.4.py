def czy_mniejszy(n, s, k1, k2):
    i = k1
    j = k2
    while i <= n and j <= n:
        if s[i - 1] == s[j - 1]:
            i = i + 1
            j = j + 1
        else:
            if s[i - 1] < s[j - 1]:
                return True
            else:
                return False
    if j <= n:
        return True
    else:
        return False


file = open('slowa4.txt')
for line in file.readlines():
    [n, s] = line.split()
    n = int(n)
    smallest_suffix_index = 1
    for i in range(2, n + 1):
        if czy_mniejszy(n, s, i, smallest_suffix_index):
            smallest_suffix_index = i
    smallest_suffix = s[smallest_suffix_index - 1:]
    print(smallest_suffix)
file.close()
