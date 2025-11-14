numeri_inseriti = []

while True:

    while True:
        dato = input("Inserisci un numero intero positivo: ")

        if dato.isdigit() and int(dato) > 0:
            numero_positivo = int(dato)
            numeri_inseriti.append(numero_positivo)   
            break

        print("Valore non valido")

    # Somma dei numeri pari
    somma_pari = 0
    for i in range(2, numero_positivo + 1, 2):
        somma_pari += i

    print("La somma dei numeri pari da 1 a", numero_positivo, "è:", somma_pari)

    # Somma dei numeri dispari
    somma_dispari = 0
    for i in range(1, numero_positivo + 1, 2):
        somma_dispari += i

    print("La somma dei numeri dispari da 1 a", numero_positivo, "è:", somma_dispari)

    # Verifica se è primo
    if numero_positivo == 1:
        print(numero_positivo, "non è un numero primo.")
    else:
        primo = True
        for i in range(2, numero_positivo):
            if numero_positivo % i == 0:
                primo = False
                break

        if primo:
            print(numero_positivo, "è un numero primo.")
        else:
            print(numero_positivo, "non è un numero primo.")

  
    ripeti = input("Vuoi inserire un altro numero? (s/n): ").lower()
    if ripeti != "s":
        break
print("Hai inserito i seguenti numeri:", numeri_inseriti)
