while True:
  print("Utknąłem w pętli.")

# będziemy przechowywać obecnie największą liczbę tutaj
największaLiczba = -999999999

# wprowadź pierwszą wartość
liczba = int(input("Wprowadź liczbę lub wpisz -1 aby zatrzymać: "))

# jeśli liczba nie jest równa -1, będziemy kontynuować
while liczba != -1:
    # czy liczba jest większa niż największaLiczba?
    if liczba > największaLiczba:
        # tak, uaktualnij największaLiczba
        największaLiczba = liczba
    # wprowadź następną liczbę
    liczba = int(input("Wprowadź liczbę lub wpisz -1 aby zatrzymać: "))

# wyświetl największaLiczba
print("Największa liczba wynosi:", największaLiczba)
