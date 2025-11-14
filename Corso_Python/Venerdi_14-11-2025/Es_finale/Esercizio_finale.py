# Gestione di un magazzino con autenticazione tramite login 

# Uso di una tupla per salvare i nomi degli utenti 
utenti = (
    ("antonio", "1234"),
    ("mirko", "1234"),
    ("mario", "1234")
)

magazzino = []
def login():
    tentativi = 3

    while tentativi > 0:
        username = input("Inserisci username: ")
        password = input("Inserisci password: ")

        if (username, password) in utenti:
            print("Login effettuato con successo")
            return True  
        
        else:
            tentativi = tentativi - 1
            print("Credenziali errate! Tentativi rimasti: " + str(tentativi))

    print("Accesso negato. Troppi tentativi.")
    return False
        
def aggiungi_prodotto():
    nome = input("Inserisci il nome del prodotto: ")
    quantita = input("Inserisci la quantità: ")

    if quantita.isdigit():
        quantita = int(quantita)
        if quantita > 0:
            magazzino.append((nome, quantita))
            print("Prodotto aggiunto")
        else:
            print("La quantità deve essere maggiore di zero")
    else:
        print("Inserire un numero valido per la quantità")

def mostra_prodotti():
    if len(magazzino) == 0:
        print("Il magazzino è vuoto")
    else:
        print("Prodotti in magazzino:")
        for prodotto in magazzino:
            print("Nome: " + prodotto[0] + ", Quantita: " + str(prodotto[1]))

def mostra_prodotti_senza_duplicati():
    if len(magazzino) == 0:
        print("Il magazzino è vuoto")
    else:
        nomi_unici = set()  
        for prodotto in magazzino:
            nomi_unici.add(prodotto[0])  
        print("Prodotti in magazzino (senza duplicati):")
        for nome in nomi_unici:
            print(nome)
loggato = False

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