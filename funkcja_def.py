def czy_parzysta(liczba):
    if liczba % 2 == 0:
        return "Parzysta"
    else:
        return "Nieparzysta"
liczba_uzytkownika = float(input("Podaj liczbe:"))
wynik = czy_parzysta(liczba_uzytkownika)
print("Wynik sprawdzenia", wynik)
