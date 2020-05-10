kwota_prog_pierwszy = 85528
ulga_podatkowa = 556.02

przychod = float(input("Wprowadz roczny przychod: "))
kwota_podatku_przy_przekroczeniua_progu = float((kwota_prog_pierwszy * 0.18) - 556.02)
podatek = 0
	
if przychod <= kwota_prog_pierwszy:
	print("biedak")
	podatek = (przychod * 0.18)
	if podatek < 0 :
		podatek = 0
else:
	print("zlodziej")
	podatek = (kwota_prog_pierwszy * 0.18)
	podatek += ((przychod - kwota_prog_pierwszy) * 0.32 )

podatek = round(przychod - ulga_podatkowa, 2)
print("Podatek wynosi: ", podatek)	

# dochod = float(input("Wprowadz roczny przychod: "))
# #
# # tutaj wpisz swój kod
# #
# podatek = round(przychod - ulga_podatkowa, 0)
# print("Podatek wynosi:", podatek)


'''
Cele

    używanie instrukcji if-else aby rozgałęzić ścieżkę kontrolną;
    budowanie programu kompletnego, który rozwiązuje proste problemy z prawdziwego życia.

Scenariusz

Dawno, dawno temu istniała kraina mlekiem i miodem płynąca, zamieszkana przez szczęśliwych i dostatnich ludzi. Ludzie oczywiście płacili podatki - ich szczęście miało ograniczenia. Najważniejszy podatek, zwany Podatkiem przychodowym (PIT w skrócie) musiał być płacony raz w roku i był obliczany zgodnie z następującą zasadą:

    jeżeli dochód obywatela nie był wyższy niż 85,528 talarów, podatek był równy 18% przychodu minus 556 talarów i 2 centy (była to tak zwana ulga podatkowa)
    jeżeli dochód był wyższy niż ta kwota, podatek był równy 14,839 talarów i 2 centy plus 32% nadwyżki ponad 85,528 talarów.

Twoim zadaniem jest napisać kalkulator podatkowy.

    Powinien on na wejściu przyjąć jedną wartość zmiennoprzecinkową: dochód.
    Następnie powinien wyświetlić obliczony podatek, zaokrąglony do pełnych talarów. Istnieje funkcja o nazwie round() która wykona za ciebie zaokrąglenie - znajdziesz ją w szkielecie kodu w edytorze.

Uwaga: ten szczęśliwy kraj nigdy nie zwraca pieniędzy swoim obywatelom. Jeżeli obliczony podatek jest mniejszy od zera, oznacza to tylko brak podatku (podatek jest równy zeru). Weź to pod uwagę podczas swoich obliczeń.

Spójrz na kod w edytorze - odczytuje on tylko jedną wartość wejściową i wyświetla wynik, więc musisz ją uzupełnić pewnymi inteligentnymi obliczeniami.

Przetestuj swój kod, korzystając z danych, które dostarczyliśmy.
Dane testowe

Przykładowe dane wejściowe: 10000

Oczekiwany wynik: Podatek wynosi: 1244.0 talarów

Przykładowe dane wejściowe: 100000

Oczekiwany wynik: Podatek wynosi: 19470.0 talarów

Przykładowe dane wejściowe: 1000

Oczekiwany wynik: Podatek wynosi: 0.0 talarów

Przykładowe dane wejściowe: -100

Oczekiwany wynik: Podatek wynosi: 0.0 talarów

    Sandbox

Code
dochód = float(input("Wprowadź roczny dochód: "))
#
# tutaj wpisz swój kod
#
podatek = round(podatek, 0)
print("Podatek wynosi:", podatek)

    Console

Prev Next
We use cookies to improve our service. By continuing to use the site, you agree to our cookie policy. × 
'''
