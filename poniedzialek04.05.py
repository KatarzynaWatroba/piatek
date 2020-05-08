print("2")
print(2)
#wartosc osemkowa
print(0o123)
print(0o213)
#wartosc szesnastkowa
print(0x123)
print(0x32134)


# znak ucieczki

print('Rok 1984 Goerge\'a Orwella.')
#float numbers
print(0.4)
print(.4)
#zapisywanie innej potegi
print("4E20")
print("3 x 108")
print(0.0000000000000000000001)
print(6.62607E-34)

#cudzyslow
print("Lubię \"Monty Pythona\"")
print('Lubię "Monty Pythona"')
print('lubie "lasice" i')

#wartosci boolowskie
print(True > False)
print(True < False)
print(1 > 0)
print(1 < 0)
#zadanie
#Scenariusz

#Napisz jedną linijkę kodu, używając funkcji print(), podwójnego cudzysłowu do zapisania łańcucha znaków (""), znaku nowej linii (\n) oraz znaku ucieczki (\), aby uzyskać oczekiwany wynik (trzy linie tekstu).



#1011= 1*2(1)+1*2(2)+0*2(3)+1*2(4)=2+4+16=22

print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)

#jeśli oba argumenty operatora ** są liczbami całkowitymi, to wynik działania jest również liczbą całkowitą;
#2.jeśli choć jeden argument operatora ** jest liczbą zmiennoprzecinkową, to wynikiem jest liczba zmiennoprzecinkowa.
#W wyniku operacji z użyciem operatora oznaczającego dzielenie zawsze otrzymujemy liczbę zmiennoprzecinkową, bez względu na to czy na pierwszy rzut oka faktycznie wynik powinien być liczbą zmiennoprzecinkową: 1 / 2, czy może liczbą całkowitą: 2 / 1.
#Podwójny ukośnik // to operator dzielenia całkowitego. Różni się on od standardowego operatora / dwoma szczegółami:
#wynik takiej operacji pozbawiony jest części dziesiętnej – nie ma jej wcale (w przypadku liczb całkowitych) albo zawsze wynosi zero (w przypadku liczb rzeczywistych). Oznacza to, że wynik zostaje zawsze zaokrąglony;
#zachowanie takie jest zgodne z zasadą liczba całkowita vs. liczba zmiennoprzecinkowa.

#zaokraglanie do wartosci mniejszej
print(6 // 4)
print(6. // 4)
print(-6 // 4)
print(6. // -4)



print(14 % 4)

#Wynikiem jest liczba dwa. Oto dlaczego:

    #14 // 4 daje 3 → wynik to iloraz w postaci liczby całkowitej;
    #3 * 4 daje 12 → wynik to rezultat mnożenia ilorazu i dzielnika;
    #14 - 12 daje 2 → wynik to reszta.

#pitagoras
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)

a = 7
b = 9
c= (a**2 + b **2) **0.5
print("c=", c)






print('"ucze sie \"')
print('""jezyka \""')
print('"""Python\"""')

