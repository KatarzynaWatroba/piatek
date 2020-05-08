# Program odczytuje sekwencję liczb i liczy ile z nich
# jest liczbami parzystymi a ile nieparzystymi.
# Program kończy pracę po wpisaniu zera.

parzyste = 0
nieparzyste = 0

# wczytaj pierwszą liczbę
liczba = int(input("Wpisz liczbę lub 0, aby zatrzymać: "))

# 0 kończy wykonywanie
while liczba != 0:
    # sprawdź czy liczba jest nieparzysta
    if liczba % 2 == 1:
        # zwiększ licznik liczb nieparzystych
        nieparzyste += 1
    else:
        # zwiększ licznik liczb parzystych
        parzyste += 1
    # wczytaj kolejną liczbę
    liczba = int(input("Wpisz liczbę lub 0, aby zatrzymać: "))

# wyświetl wynik
print("Liczb nieparzystych:", nieparzyste)
print("Liczb parzystych:", parzyste)
