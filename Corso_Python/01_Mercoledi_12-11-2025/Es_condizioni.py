numero = -10
# Verifica se il numero è positivo o negativo
if numero > 0:
    print("Il numero è positivo.")
else:
    print("Il numero è negativo.")
    
# Verifica se un numero è pari o dispari
x = 4    
if (x >0):
    print("x è positivo")
    if (x % 2 == 0):
        print("x è anche pari")
    else:
        print("x è dispari")            
else:
    print("x è negativo")   
    
# Verifica se un numero è positivo, negativo o zero
numero = -7
if numero > 0:
    print("Il numero è positivo.")
    if numero == 100:
        print("Wow")
elif numero < 0:  
    print("Il numero è negativo.")  
else:
    print("Il numero è zero.")
        
        
# Verifica se un numero è positivo, negativo o zero


x = int(input("Inserisci un numero: "))
if x == 150:
    print("Hai Vinto!")
    if x == 100:
        print("Troppo basso")    
elif x == 200:  
    print("Hai perso.")  
    
    
    
print("1. Crea elemento")
print("2. Aggiorna elemento")
print("3. Elimina elemento")
print("0. Esci")

scelta = input("Seleziona un'opzione: ")

if scelta == "1":
    print("Hai scelto di CREARE un nuovo elemento.")
    nome = input("Inserisci il nome: ")

elif scelta == "2":
    print("Hai scelto di AGGIORNARE un elemento.")
    nomeAggiornato = input("Digita il nuovo nome: ")       
    nome = nomeAggiornato
    print("Nome aggiornato a:", nome)
elif scelta == "3":
    print("Hai scelto di ELIMINARE un elemento.")
    scelta = input("Sei sicuro?: [S/N]")   
    if scelta.upper() == "S":
        print("Elemento eliminato.")
        nome = ""
    else:
        print("Eliminazione annullata.")    

elif scelta == "0":
    print("Uscita dal programma...")

else:
    print("Scelta non valida!")
    
    
# Esercizio 3
nome_utente = input("Inserisci il tuo nome utente: ")
password_utente = input("Inserisci la tua password: ")  
id = 1
if nome_utente == "utente" and password_utente == "1234":
    print("Accesso consentito.")
else:
    print("Accesso negato.")
# altro modo per esercizio 3
accesso = input("Digita 1 per accedere: ")
if(accesso == "1"):
    nome_utente = input("Inserisci il tuo nome utente: ")
    password_utente = input("Inserisci la tua password: ")  
    if nome_utente == "utente" and password_utente == "1234":
        print("Accesso consentito.")
    else:
        print("Accesso negato.")
        
        
# Esercizio 4

comando = input("Inserisci un comando: ")
match comando:
    case "start":
        print("Avvio del programma.")
    case "stop":
        print("Chiusura del programma.")
    case "pause":
        print("Programma in pausa...")
    case _:
        print("Comando non riconosciuto.")