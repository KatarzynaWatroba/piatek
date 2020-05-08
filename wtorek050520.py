#x = x * 2
#owce = owce + 1
#x *= 2
#owca += 1

kilometry = 12.25
mile = 7.38

mile_na_kilometry =  7.38 * 1.61
kilometry_na_mile =  12.25 / 1.61


print(mile, "mi to", round(mile_na_kilometry, 2), "km")
print(kilometry, "km to", round(kilometry_na_mile, 2), "mi")

#przelicznik; 1 lasica = 1,3 borsuka
borsuk = 34
lasica = 27

lasice_na_borsuki = 27 * 1.3
borsuki_na_lasica = 34 / 1.3

print(lasica, "dokladnie", round(lasice_na_borsuki), "bez jednostek")
print(borsuk, "zamiana", round(borsuki_na_lasica), "bez jednostek")


 LABORATORIUM

Przewidywany czas

10-15 minut
Poziom trudności

Łatwy
Cele

    zapoznanie się z konceptem liczb, operatorów i operacji matematycznych w języku Python;
    wykonywanie podstawowych obliczeń.

Scenariusz

Spójrz na kod w edytorze: sczytuje on wartość typu float, przypisuje ją do zmiennej xi wypisuje wartość przypisaną do zmiennej y. Twoim zadaniem jest uzupełnienie kodu w celu obliczenia następującego wyrażenia:

3x3 - 2x2 + 3x - 1

Wynik powinien zostać przypisany do zmiennej y.

Pamiętaj, że klasyczny zapis algebraiczny często pomija operator mnożenia - musisz więc go użyć w swoim kodzie. Zwróć uwagę, jak zmieniamy typ danych, aby się upewnić, że x jest liczbą zmiennoprzecinkową.

Zachowaj czysty i czytelny kod i przetestuj go za pomocą dostarczonych danych, za każdym razem przypisując je do zmiennej x (poprzez zakodowanie wartości na sztywno). Nie zniechęcaj się żadnymi początkowymi błędami. Bądź wytrwały i dociekliwy.
Dane Testowe

Przykładowe dane wejściowe
x = 0
x = 1
x = -1

Oczekiwany wynik
y = -1.0
y = 3.0
y = -9.0

    Sandbox

Code
x = # Tutaj wprowadź swoje dane testowe.
x = float(x)

# Tutaj napisz swój kod.

print("y =", y)

    Console

Prev Next
We use cookies to improve our service. By continuing to use the site, you agree to our cookie policy. × 

x =  # Tutaj wprowadź swoje dane testowe.
x = float(x)

# Tutaj napisz swój kod.

print("y =", y)
