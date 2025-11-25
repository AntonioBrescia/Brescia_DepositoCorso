# Gestione di un magazzino con autenticazione tramite login 
from Funzioni import *
while True:
    if loggato == False:
        scelta = input("Benvenuto nel sistema! Premi [1] per accedere, [2] per uscire: ")
        if scelta == "1":
            loggato = login()
            if loggato == False:
                print("Login fallito, programma terminato")
                break
        elif scelta == "2":
            print("Ciao!")
            break
        else:
            print("Scelta non valida")
    else:
        print("MENU MAGAZZINO")
        print("1 - Aggiungi prodotto")
        print("2 - Vedi prodotti")
        print("3 - Vedi prodotti non duplicati")
        print("4 - Esci")

        opzione = input("Scegli un'opzione: ")

        match opzione:
            case "1":
                aggiungi_prodotto()
            case "2":
                mostra_prodotti()
            case "3":
                mostra_prodotti_senza_duplicati()
            case "4":
                print("Arrivederci")
                loggato = False 
            case _:
                print("Opzione non valida!")