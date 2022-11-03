gracz_1 =input("Podaj imie gracza 1:")
gracz_2 =input("Podaj imie gracza 2:")

gracz_1_odp = input(' %s: Wybierz kamień, papier lub nożyczki: '%gracz_1)
gracz_2_odp = input(' %s: Wybierz kamień, papier lub nożyczki: '%gracz_2)

def porownaj(odp_1, odp_2):
    if odp_1 == odp_2:
        return("remis")
    elif odp_1 == "kamien":
        if odp_2 == "nozyczki":
            return ("Wygrywa kamień! Gracz: %s "%gracz_1)
        else:
            return("Wygrywa papier! Gracz: %s" %gracz_2)

    elif odp_1 == "nozyczki":
        if odp_2 == "papier":
            return("Wygrywaja nożyczki! Gracz:%s "%gracz_1)
        else:
            return("Wygrywa kamień! Gracz: %s" %gracz_2)

    elif odp_1 == "papier":
        if odp_2 == "kamien":
            return("Wygrywa papier! Gracz:%s "%gracz_1)
        else:
            return("Wygrywaja nożyczki! Gracz: %s" %gracz_2)
    else:
        print("zły wybór")   



print(porownaj(gracz_1_odp,gracz_2_odp))
