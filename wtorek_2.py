a = '1'
b = "1"
print(a + b)
a = 6
b = 3
a /= 2 * b
print(a)
print("Powiedz mi cokolwiek...")
cokolwiek = input()
print("Hmm...", cokolwiek, "... Serio?")

cokolwiek = input("Powiedz mi cokolwiek...")
print("Hmm...", cokolwiek, "...Serio?")

cokolwiek = input("Powiedz mi cokolwiek...")
print("Hmm...", cokolwiek, "...Serio?")

cokolwiek = input("Wpisz dowolną liczbę: ")
coś = cokolwiek ** 2.0
print(cokolwiek, "do potęgi 2 wynosi", coś)


#zadanie z float i  int

cokolwiek = float(input("Wpisz liczbę: "))
coś = cokolwiek ** 2.0
print(cokolwiek, "do potęgi 2 wynosi", coś)


#przelicznik wieku na miesiace

wiek = float(input("ile masz lat?: "))
miesice = wiek * 12
print(wiek, "to w miesiacach", miesice)

#dlugosc przeciwprostokatnej
bok_a = float(input("Wprowadź długość pierwszego boku: "))
bok_b = float(input("Wprowadź długość drugiego boku: "))
przeciwprostokątna = (bok_a**2 + bok_b**2) ** .5
print("Długość przeciwprostokątnej wynosi", przeciwprostokątna)




#rysowanie prostokata
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")
