#zadanie 
#Scenariusz
#Spathiphyllum, bardziej znany jako skrzydłokwiat, jest jedną z najbardziej popularnych domowych #roślin doniczkowych, które filtrują szkodliwe toksyny z powietrza. Niektóre z neutralizowanych #przez nią toksyn to benzen, formaldehyd i amoniak.
#Wyobraź sobie, że twój program komputerowy uwielbia te rośliny. Za każdym razem, gdy otrzymuje #dane wejściowe w postaci słowa Skrzydłokwiat, mimowolnie wysyła do konsoli następujący ciąg #znaków: "Skrzydłokwiat jest najlepszą rośliną w historii!"
#Napisz program, który wykorzystuje koncepcję warunkowego wykonywania, pobiera ciąg znaków jako #dane wejściowe i wypisuje w konsoli zdanie "Skrzydłokwiat jest najlepszą rośliną w historii!" #jeżeli danymi wejściowymi jest słowo "Skrzydłokwiat" (zwróć uwagę na pierwszą dużą literę), a w #innym wypadku wyświetla komunikat: "Nie, ja chcę Skrzydłokwiat...!".
#Przetestuj swój kod, korzystając z danych, które dla ciebie 


kwiatek = input("wpisz swoja ulubiona nazwe kwiatka: ")
if kwiatek == "Skrzydlokwiat" :
	print("skrzydlokwiat jest najlepsza roslina w historii!")
else:
	print("nie, ja chce skrzydlokwiat...!") 
