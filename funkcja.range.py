
for i in range (4, 2, 9):
    print("wartosc i wynosi obecnie", i)

pow = 1
for exp in range(16):
    print("2 do potęgi", exp, "wynosi", pow)
    pow *= 2

Zmienna exp jest używana jako zmienna kontrolna pętli, i określa ona bieżącą wartość wykładnika. Samo potęgowanie zostaje zastąpione przez pomnożenie przez dwa. Ponieważ 20 jest równe 1, to 2 × 1 wynosi 21, 2 × 21 wynosi 22, i tak dalej. Jaki jest największy wykładnik, dla którego nasz program nadal wyświetli wynik
