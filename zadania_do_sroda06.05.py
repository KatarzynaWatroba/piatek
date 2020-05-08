
#if ladnaPogoda:
#    pojdziemyNaSpacer()
#zjemyLunch()
licznikOwiec = input("wpisz ilosc owiec: ")
if int(licznikOwiec) >= 120: # porównanie wyrażenia
      # wykonuje wyrażenie jeżeli wynikiem porównania jest True
	#spijsobie(licznikOwiec)
#if ładnaPogoda:
 #   pójdziemyNaSpacer()
#else:
 #   pójdziemyDoKina()
#zjemyLunch()

#zadanie 2 z liczbami:

# przeczytaj dwie liczby
liczba1 = int(input("Wprowadź pierwszą liczbę: "))
liczba2 = int(input("Wprowadź drugą liczbę: "))

# wybierz większą liczbę
if liczba1 > liczba2:
    większaLiczba = liczba1
else:
    większaLiczba = liczba2

# wyświetl wynik
print("Większą liczbą jest:", większaLiczba)

#zadanie z liczbami, rozwiazanie z 3 zmiennymi

# przeczytaj trzy liczby
liczba1 = int(input("Wprowadź pierwszą liczbę: "))
liczba2 = int(input("Wprowadź drugą liczbę: "))
liczba3 = int(input("Wprowadź trzecią liczbę: "))

# tymczasowo zakładamy, że pierwszy numer
# jest największa
# sprawdzimy to wkrótce
największaLiczba = liczba1

# sprawdzamy, czy druga liczba jest większa niż obecna największaLiczba
# i uaktualniamy największaLiczba jeżeli zachodzi taka potrzeba
if liczba2 > największaLiczba:
    największaLiczba = liczba2

# sprawdzamy, czy trzecia liczba jest większa niż obecna największaLiczba
# i uaktualniamy największaLiczba jeżeli zachodzi taka potrzeba
if liczba3 > największaLiczba:
    największaLiczba = liczba3

# wyświetlamy wynik
print("Największą liczbą jest:", największaLiczba)


#Oto przykład pseudokodu:
line 01 largestNumber = -999999999
line 02 liczba = int(input())
line 03 if liczba == -1:
line 04     print(największaLiczba)
line 05     zakończ()
line 06 if liczba > największaLiczba:
line 07     największaLiczba = liczba
line 08 przejdź do linii 02
