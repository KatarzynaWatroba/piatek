kalendarz gregorianski

Poziom trudności

Łatwy/średni
Cele

    używanie instrukcji if-elif-else;
    znalezienie właściwej implementacji dla sformułowanych reguł;
    testowanie kodu za pomocą przykładowego wejścia i wyjścia.

Scenariusz

Jak zapewne wiesz, z pewnych astronomicznych powodów lata mogą być przestępne lub zwykłe. Te pierwsze mają 366 dni, a drugie 365 dni.

Od czasu wprowadzenia kalendarza gregoriańskiego (w 1582 roku), zasada ta służy do określenia rodzaju roku:

    jeśli rok nie jest podzielny przez cztery, jest to zwykły rok;
    w przeciwnym razie, jeśli rok nie jest podzielny przez 100, jest to rok przestępny;
    w przeciwnym razie, jeśli rok nie jest podzielny przez 400, jest to zwykły rok;
    w przeciwnym razie jest to rok przestępny.

Spójrz na kod w edytorze - odczytuje on tylko rok i musi zostać uzupełniony instrukcjami implementującymi test, który właśnie opisaliśmy.

Kod powinien wypisać jeden z dwóch możliwych komunikatów, czyli Rok przestępny lub Rok zwykły, w zależności od wprowadzonej wartości.

Sprawdź także czy wypisany rok należy do epoki gregoriańskiej i wyświetl ostrzeżenie jeśli tak nie jest: Nie w kalendarzu gregoriańskim. Podpowiedź: użyj operatorów != oraz %.

Przetestuj swój kod, korzystając z danych, które dostarczyliśmy.
Dane testowe

Przykładowe dane wejściowe: 2000

Oczekiwany wynik: Rok przestępny

Przykładowe dane wejściowe: 2015

Oczekiwany wynik: Rok zwykły

Przykładowe dane wejściowe: 1999

Oczekiwany wynik: Rok zwykły

Przykładowe dane wejściowe: 1996

Oczekiwany wynik: Rok przestępny

Przykładowe dane wejściowe: 1580

Oczekiwany wynik: Nie w kalendarzu gregoriańskim

    Sandbox

Code
rok = int(input("Wprowadź rok: "))
#
# tutaj wpisz swój kod
#

    Console

Prev Next
We use cookies to improve our service. By continuing to use the site, you agree to our cookie policy. × 
