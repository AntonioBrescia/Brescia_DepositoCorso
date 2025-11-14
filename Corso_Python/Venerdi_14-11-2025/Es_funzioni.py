import random
# funzioni con tipo di ritorno nullo 
def saluta(nome):
    print("ciao ",nome)
    
saluta("Antonio")

def somma(a, b):
    risultato = a +b
    print("La somma è:", risultato)
    
somma(5,6)

# funzioni con tipo di ritorno definito 

def quadrato(numero):
    return numero * numero 

risultato = quadrato(2)
print(risultato)


# Esercizio 1 
def indovinaNumero():
    while True:
        numero_casuale = random.randint(1, 100)
        while True:
            inputUtente = int(input("Inserisci un numero: "))
            
            if inputUtente == numero_casuale:
                print("Complimenti! Hai indovinato!")
                break
            elif inputUtente < numero_casuale:
                print("Troppo basso, riprova.")
            else:
                print("Troppo alto, riprova.")
        gioca_ancora = input("Vuoi giocare di nuovo? (s/n): ").lower()
        if gioca_ancora != 's':
            print("Arrivederci")
            break
        
indovinaNumero()


#Esercizio 2 
def sequenza_fibonacci():
    
    while True:
        n = int(input("Quanti numeri della sequenza di Fibonacci vuoi? "))
        a=  0
        b = 1
        for i in range(n):
            print(a, end=" ")
            c = a
            a = b
            b = c + b
        print()  
        
        gioca_ancora = input("Vuoi giocare di nuovo? (s/n): ").lower()
        if gioca_ancora != 's':
            print("Arrivederci")
            break
        
sequenza_fibonacci()