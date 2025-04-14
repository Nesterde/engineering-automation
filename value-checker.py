#funkcja, w której warunek też będzie zależeć od użytkownika
def mniejsza(liczba, warunek):
    if liczba < warunek:
        return f"twoja wskazana liczba {liczba} jest mniejsza od {warunek}"
    else:
        return f"twoja wskazana liczba {liczba} jest wieksza od {warunek}"
warunek = float(input("wpisz liczbe warunku: "))
twoja_liczba = float(input("wpisz swoja liczbe do sprawdzenia: "))
wynik = mniejsza(twoja_liczba, warunek)
print(wynik)