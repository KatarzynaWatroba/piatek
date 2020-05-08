var = 9
var == 0

czarnaowca = 2
bialaowca = 3

print(czarnaowca > bialaowca)
print(bialaowca > czarnaowca)
temperaturaNaZewnatrz = 31
print(temperaturaNaZewnatrz >= 0.0) # większe bądź równe)


liczbaLwow = input("wymysl liczbe lwow: ")
liczbaLwic = input("wymysl liczbe lwic: ")
print(  liczbaLwow >= liczbaLwic)

#zadanie 1
#Używając jednego z operatorów porównania w Pythonie, napisz prosty dwuliniowy program, który #przyjmuje parametr n jako dane wejściowe, będące liczbą całkowitą, i wypisuje w konsoli False #jeżeli n jest mniejsze niż 100, lub True jeżeli n jest większe lub równe 100.
#Przetestuj swój kod korzystając z danych, które dla ciebie przygotowaliśmy.

#Dane Testowe
#Przykładowe dane wejściowe: 55
#Oczekiwany wynik: False
#Przykładowe dane wejściowe: 99
#Oczekiwany wynik: False
#Przykładowe dane wejściowe: 100
#Oczekiwany wynik: True
#Przykładowe dane wejściowe: 101
#Oczekiwany wynik: True
#Przykładowe dane wejściowe: -5
#Oczekiwany wynik: False
#Przykładowe dane wejściowe: +123
#Oczekiwany wynik: False

#moj kod:

n = input("write your favourite number: ")
print(int(n) >= 100





#funkcja if:
#Ta instrukcja warunkowa składa się z następujących, niezbędnych elementów, które wymagają tej #właśnie kolejności:

#słowo kluczowe if (jeśli),
#jeden lub więcej białych znaków,
#wyrażenie (pytanie lub odpowiedź), którego wartość będzie interpretowana wyłącznie w kategoriach #True (gdy jego wartość jest różna od zera) i False (gdy jest równa zeru);
#dwukropek po którym następuje nowa linia;
#instrukcja lub zestaw instrukcji umieszczony po wcięciu (bezwzględnie wymagana jest co najmniej #jedna instrukcja); wcięcie można osiągnąć na dwa sposoby – wstawiając określoną liczbę spacji #(zalecane jest użycie czterech spacji), lub używając znaku tabulacji; uwaga: jeśli we fragmencie #kodu umieszczonym po wcięciu znajduje się więcej niż jedna instrukcja, wcięcie powinno być #dokładnie takie same we wszystkich liniach - Python 3 nie pozwala na mieszanie spacji i tabulacji #do tworzenia wcięć.
#Jak działa ta instrukcja?
#Jeżeli wyrażenie prawda_lub_fałsz reprezentuje prawdę (tj. jego wartość nie jest równa zeru), #wykonany zostanie fragment kodu umieszczony we wcięciu;
#Jeżeli wyrażenie prawda_lub_fałsz nie reprezentuje prawdy (tj. jego wartość jest równa zeru), #fragment kodu umieszczony we wcięciu zostanie pominięty (zignorowany), a następną wykonaną #instrukcją będzie ta, która wystąpi po pierwotnym poziomie wcięcia.





Instrukcja elif

Drugi specjalny przypadek wprowadza kolejne nowe słowo kluczowe języka Python: elif. ak pewnie podejrzewasz, jest ono krótszą formą else if.

Słowo elif jest używane do sprawdzania więcej niż jednego warunku, oraz do zatrzymania gdy zostanie znalezione pierwsze prawdziwe twierdzenie.

Nasz następny przykład przypomina zagnieżdżanie, jednak podobieństwa są bardzo niewielkie. Ponownie zmieniamy nasze plany i wyrażamy je w następujący sposób: Jeśli będzie ładnie, pójdziemy na spacer, w przeciwnym razie jeśli dostaniemy bilety, pójdziemy do kina, w przeciwnym razie, jeśli dostaniemy stolik w restauracji, pójdziemy na lunch; jeśli wszystko inne zawiedzie, wracamy do domu i gramy w szachy.

Czy zauważyłeś, ile razy użyliśmy słów w przeciwnym razie? To jest etap, w którym słowo kluczowe elif odgrywa swoją rolę.



