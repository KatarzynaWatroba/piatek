tajnyNumer = 777

'''
Define procedure (function) as this code repeats more than one time.
This function will prompt user about integer number and if user not 
provide correct then will inform him and prompt again until provide
any integer value.
'''
def takeCorrectNumberFromUserOrKillHim():
	numerOdUzytkownika = input("wprowadz liczbe calkowita: ")
	while not numerOdUzytkownika.isdigit():
		print("Debil, \"",numerOdUzytkownika,"\" to nie jest liczba calokowita!")
		numerOdUzytkownika = input("Kolejna szansa, wprowadz liczbe calkowita: ")
	return int(numerOdUzytkownika)

	

'''
This is program body. Program will stck in this loop until user 
provide correct number defined in variable named "tajnyNumer"
'''
while tajnyNumer != numerOdUzytkownika:
	print("Nietrafione")
	numerOdUzytkownika = takeCorrectNumberFromUserOrKillHim()
	
print("Brawo dobra robota")