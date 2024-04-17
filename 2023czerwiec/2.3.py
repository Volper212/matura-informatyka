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


def merge_sort(sufiksy, od, do, n, s):
    if do - od == 1:
        if not czy_mniejszy(n, s, sufiksy[od - 1], sufiksy[do - 1]):
            pomocnicza = sufiksy[od - 1]
            sufiksy[od - 1] = sufiksy[do - 1]
            sufiksy[do - 1] = pomocnicza
    elif do - od > 1:
        punkt_podzialu = (do + od) // 2
        merge_sort(sufiksy, od, punkt_podzialu, n, s)
        merge_sort(sufiksy, punkt_podzialu + 1, do, n, s)
        lewe_sufiksy = []
        i = od
        while i <= punkt_podzialu:
            lewe_sufiksy.append(sufiksy[i - 1])
            i = i + 1
        j = punkt_podzialu + 1
        prawe_sufiksy = []
        while j <= do:
            prawe_sufiksy.append(sufiksy[j - 1])
            j = j + 1
        i = 1
        j = 1
        for k in range(od, do + 1):
            if i > len(lewe_sufiksy):
                sufiksy[k - 1] = prawe_sufiksy[j - 1]
                j += 1
            elif j > len(prawe_sufiksy):
                sufiksy[k - 1] = lewe_sufiksy[i - 1]
                i += 1
            else:
                lewy_sufiks = lewe_sufiksy[i - 1]
                prawy_sufiks = prawe_sufiksy[j - 1]
                if czy_mniejszy(n, s, prawy_sufiks, lewy_sufiks):
                    sufiksy[k - 1] = prawy_sufiks
                    j += 1
                else:
                    sufiksy[k - 1] = lewy_sufiks
                    i += 1


n = 10
s = "mascarpone"
T = [0]*n
i = 1
while i <= n:
    T[i - 1] = i
    i = i + 1
i = 1
while i < n:
    j = 1
    while j <= n - i:
        if czy_mniejszy(n, s, T[j - 1 + 1], T[j - 1]):
            pomocnicza = T[j - 1]
            T[j - 1] = T[j - 1 + 1]
            T[j - 1 + 1] = pomocnicza
        j = j + 1
    i = i + 1
print(T)
