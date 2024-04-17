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


with open("slowa1.txt") as file:
    lines = [line.strip() for line in file.readlines()]
    n = int(lines[0])
    s = lines[1]
    [k1, k2] = [int(suffixIndex) for suffixIndex in lines[2].split()]
    print("TAK" if czy_mniejszy(n, s, k1, k2) else "NIE")
