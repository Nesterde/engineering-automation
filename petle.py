# LEKCJA 4: PĘTLE W PYTHONIE

# PĘTLA WHILE:
# Wykonuje kod dopóki warunek jest spełniony (czyli "True")

x = float(input("Podaj liczbe startowa:"))  # Startowa wartość zmiennej x

while x <= 10:  # Pętla będzie działać dopóki x jest mniejsze lub równe 10
    print("Wartość x:", x)  # Wyświetlamy aktualną wartość x
    x += 1  # Zwiększamy x o 1 przy każdym obrocie pętli

print("---")  # Oddzielenie wyników


# PĘTLA FOR:
# Używana do przechodzenia przez kolejne elementy (np. liczby, znaki, listy)

# range(1, 11) oznacza liczby od 1 do 10 (11 jest pomijane)
for i in range(1, 11):
    print("Liczba z pętli for:", i)

print("---")  # Oddzielenie wyników


# MINI PROJEKT: SUMA LICZB OD 1 DO N

# Zapytaj użytkownika o liczbę
n = int(input("Podaj liczbę n: "))

suma = 0  # Tu będziemy dodawać kolejne liczby

# Dla każdej liczby od 1 do n, dodaj ją do sumy
for liczba in range(1, n + 1):
    print(liczba)  # Wyświetlamy aktualną liczbę
    suma += liczba  # Dodajemy ją do sumy

# Na koniec wyświetlamy sumę
print("Suma liczb od 1 do", n, "to:", suma)
