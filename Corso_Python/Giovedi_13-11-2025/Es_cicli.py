#ciclo matematico 
conteggio = 0

while conteggio < 5: 
    print(conteggio)
    conteggio += 1
print("-----------------------------------------------")   
# ciclo booleano
controllo = False
while controllo:
    print(controllo)
    scelta = input("vuoi continuare?")
    if scelta.lower() == "no":
        controllo = False       
    else:
        print("Stai continuando")
print("-----------------------------------------------")   
# ciclo for 
numeri = [1,2,3,4,5]
for numero in numeri:
    print(numero)
        
print("-----------------------------------------------")   

#range
for i in range(5):
    print(i)
    

for i in range(1,10,2):
    print(i)


# Esercizio conto alla rovescia 
ripetere = True
while ripetere:  # ciclo infinito per permettere all'utente di ripetere il programma
    numero = int(input("Inserisci un numero: "))  # chiedi all'utente di inserire un numero 

    for i in range(numero, 0, -1):  # ciclo che parte dal numero inserito e scende fino a 1
        print(i)  # stampa ogni numero del conto alla rovescia

    ripeti = input("Vuoi ripetere? (s/n): ").lower()  # chiedi se l'utente vuole ripetere e converte la risposta in minuscolo
    if ripeti != 's':  # se la risposta non è "s", interrompi il ciclo
        print("Programma terminato.")  # messaggio di fine programma
        ripetere = False    #variabile passata a false 
    
    
# Esercizio controllo numero primo pari o dispari 


# Creiamo una lista vuota per salvare i numeri inseriti dall'utente
listaNumeri = []

# Ciclo finché non sono stati inseriti 5 numeri
while len(listaNumeri) < 5:
    numero = int(input("Inserisci un numero: "))  # chiediamo un numero intero
    listaNumeri.append(numero)  # aggiungiamo il numero alla lista
    # Controllo se il numero è primo
    if numero < 2:
        # I numeri minori di 2 non sono primi
        print("Il numero non è primo.")
    else:
        primo = True 
        # Ciclo per verificare se esiste un divisore tra 2 e radice quadrata del numero
        i = 2
        while i <= int(numero ** 0.5):
            if numero % i == 0:
                primo = False  # se troviamo un divisore, il numero non è primo
            i += 1  # incrementiamo i per continuare il controllo

        # Stampa se il numero è primo o no
        if primo:
            print(str(numero) + " è primo.")
        else:
            print(str(numero) + " non è primo.")

    # Controllo se il numero è pari o dispari
    if numero % 2 == 0:
        print(str(numero) + " è pari.")
    else:
        print(str(numero) + " è dispari.")

# Stampiamo tutti i numeri inseriti dall'utente
print("\nHai inserito:", listaNumeri)



# Salva 5 numeri pari (Esempio di Mirko)
pari_trovati = []   # lista dei numeri pari salvati

# il ciclo continua finché non abbiamo 5 numeri pari
while len(pari_trovati) < 5:

    numero_input = input("Inserisci un numero: ")
    numero = int(numero_input)

    # controllo pari
    if numero % 2 == 0:
        print("Il numero è pari.")
        pari_trovati.append(numero)
        print("Numeri pari salvati:", pari_trovati)
    else:
        print("Il numero non è pari.")

print("Hai trovato 5 numeri pari!")
print("Lista finale:", pari_trovati)

