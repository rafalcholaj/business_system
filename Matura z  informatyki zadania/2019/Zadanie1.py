# dane (są w zadaniu, nie trzeba ich uwzględniać w rozwiązaniu na maturze)
n = 10
A = [None, 5, 99, 3, 7, 111, 13, 4, 24, 4, 8]

# wyszukiwanie binarne
def szukaj_binarnie(A):
    lewy, prawy = 1, n
    while lewy < prawy:
        srodkowy = (lewy+prawy)//2
        if A[srodkowy]%2 != 0:  # jeśli środkowy jest nieparzysty
            lewy = srodkowy + 1
        else:                   # jeśli środkowy jest parzysty
            prawy = srodkowy
    return A[prawy]