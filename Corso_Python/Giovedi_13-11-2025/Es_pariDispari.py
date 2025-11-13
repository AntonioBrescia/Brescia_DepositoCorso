ripeti = True

while ripeti:
    scelta = input("[1] Inserisci una stringa [2] Inserisci un numero\nScelta: ")

    match scelta:
        case "1":
            stringa = input("Inserisci la stringa: ")
            lunghezzaStringa = len(stringa)

            if lunghezzaStringa % 2 == 0:
                print("La stringa ha una lunghezza pari.")
            else:
                print("La stringa ha una lunghezza dispari.")

        case "2":
            try:
                numero = int(input("Inserisci un numero: "))
                if numero % 2 == 0:
                    print("Il numero è pari.")
                else:
                    print("Il numero è dispari.")
            except ValueError:
                print("Errore: non hai inserito un numero valido.")

        case _:
            print("Scelta non valida.")

    risposta = input("Vuoi ripetere? (s/n): ")
    if risposta != "s":
        ripeti = False
        print("Programma terminato.")



# esercizio 2 

# Chiediamo all'utente di inserire due numeri
numero1 = int(input("Digita il primo numero: "))
numero2 = int(input("Digita il secondo numero: "))

# Se il primo numero è maggiore del secondo, scambiamo i numeri
if numero1 > numero2:
    numero1, numero2 = numero2, numero1

# Stampo tutti i numeri dell'intervallo
print("\nTutti i numeri:")
for n in range(numero1, numero2 + 1): 
    print(n)  
# Stampiamo i numeri primi
print("Numeri primi:")
for n in range(numero1, numero2 + 1):  # cicliamo tutti i numeri
    if n > 1:  # i numeri minori di 2 non sono primi
        primo = True  # assumiamo inizialmente che il numero sia primo
        # controlliamo se esiste un divisore tra 2 e sqrt(n)
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:  # se troviamo un divisore
                primo = False  # non è primo
                break  # usciamo dal ciclo
        if primo:  # se è rimasto primo
            print(n)
print()  # a capo dopo tutti i numeri primi

# Stampiamo i numeri non primi
print("Numeri non primi:")
for n in range(numero1, numero2 + 1):
    if n < 2:  # 0 e 1 non sono primi
        print(n)
    else:
        primo = True  # assumiamo che sia primo
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:  # se troviamo un divisore
                primo = False
                break
        if not primo:  # se non è primo
            print(n)


# altro metodo per secondo es
numero1 = int(input("Digita il primo numero: "))
numero2 = int(input("Digita il secondo numero: "))

if numero1 > numero2:
    numero1, numero2 = numero2, numero1

print("\nRisultati dei numeri nell'intervallo:")

for n in range(numero1, numero2 + 1):
    if n < 2:
        tipo = "non primo"
    else:
        primo = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                primo = False
                break
        if primo:
            tipo = "primo"
        else:
            tipo = "non primo"
    
    print(str(n) + " (" + tipo + ")", end=" ")

print()