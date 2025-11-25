""" numero1 = float(input("Inserisci il primo numero: "))
operazione = input("Scegli l'operazione (+, -, *, /): ")
numero2 = float(input("Inserisci il secondo numero: "))
# Esempio con match 
match operazione:
    case "+":
        risultato = numero1 + numero2
        print("Il risultato di " + str(numero1) + " + " + str(numero2) + " è: " + str(risultato))
    case "-":
        risultato = numero1 - numero2
        print("Il risultato di " + str(numero1) + " - " + str(numero2) + " è: " + str(risultato))
    case "*":
        risultato = numero1 * numero2
        print("Il risultato di " + str(numero1) + " * " + str(numero2) + " è: " + str(risultato))
    case "/":
        if numero2 != 0:
            risultato = numero1 / numero2
            print("Il risultato di " + str(numero1) + " / " + str(numero2) + " è: " + str(risultato))
        else:
            print("Errore: divisione per zero.")
    case _:
        print("Operazione non valida.")
 """

# Esempio con if-elif-else
numero1 = float(input("Inserisci il primo numero: "))   
operazione = input("Scegli l'operazione (+, -, *, /): ")
numero2 = float(input("Inserisci il secondo numero: "))

if operazione == "+":   
    risultato = numero1 + numero2
    print("Il risultato di " + str(numero1) + " + " + str(numero2) + " è: " + str(risultato))
elif operazione == "-": 
    risultato = numero1 - numero2
    print("Il risultato di " + str(numero1) + " - " + str(numero2) + " è: " + str(risultato))   
elif operazione == "*":
    risultato = numero1 * numero2
    print("Il risultato di " + str(numero1) + " * " + str(numero2) + " è: " + str(risultato))   
elif operazione == "/":
    if numero2 != 0:
        risultato = numero1 / numero2
        print("Il risultato di " + str(numero1) + " / " + str(numero2) + " è: " + str(risultato))
    else:
        print("Errore: divisione per zero.")
else:
    print("Operazione non valida.")


