# Es 1 Utilizzo di if
numero = int(input("Inserisci un numero:"))
if numero % 2 == 0:
    print("Il numero è pari")
else:    
    print("il numero è dispari")
    
    
    
#Es 2 Utilizzo di while e range 

ripetere = True
while ripetere:  # ciclo infinito per permettere all'utente di ripetere il programma
    numero = int(input("Inserisci un numero: "))  # chiedi all'utente di inserire un numero 
    if(numero > 0):
        for i in range(numero, -1, -1):  # ciclo che parte dal numero inserito e scende fino a 1
          print(i)  # stampa ogni numero del conto alla rovescia

    ripeti = input("Vuoi ripetere? (s/n): ").lower()  # chiedi se l'utente vuole ripetere e converte la risposta in minuscolo
    if ripeti != 's':  # se la risposta non è "s", interrompi il ciclo
        print("Programma terminato.")  # messaggio di fine programma
        ripetere = False    #variabile passata a false 
        
#Es 3 Utilizzo di for 

lista = []
listaQuadrati = []
numeri = int(input("Scegli quanti numeri inserire:"))
for i in range(numeri):
    numero = int(input("Inserisci il numero " + str(i+1) + ": "))
    lista.append(numero)
    listaQuadrati.append(numero * numero)

print("Lista numeri:", lista)
print("Lista quadrati:", listaQuadrati)


# Esercizio 4

# lista vuota dove inseriremo i numeri
lista = []

# Ciclo per chiedere all'utente di inserire 5 numeri
for i in range(5):
    numero = int(input("Inserisci il numero " + str(i+1) + ": "))
    # Aggiungiamo il numero inserito alla lista
    lista.append(numero)

# Controlliamo se la lista è vuota
if len(lista) == 0:
    # Se la lista è vuota, stampiamo un messaggio
    print("Lista vuota")
else:
    # Calcolo del numero massimo nella lista
    # Inizializziamo il massimo con il primo elemento della lista
    massimo = lista[0]
    # Ciclo per confrontare ogni numero con il massimo attuale
    for num in lista:
        # Se troviamo un numero maggiore del massimo, aggiorniamo il massimo
        if num > massimo:
            massimo = num
    # Stampiamo il numero massimo trovato
    print("Numero massimo:", massimo)

    # Calcolo del numero di elementi nella lista
    contatore = 0  # contatore a 0
    indice = 0     # indice a 0
    # Ciclo while per contare tutti gli elementi della lista
    while indice < len(lista):
        contatore += 1  # Incrementiamo il contatore
        indice += 1     # Passiamo all'elemento successivo
    # Stampiamo il numero totale di elementi nella lista
    print("Numero di elementi nella lista:", contatore)