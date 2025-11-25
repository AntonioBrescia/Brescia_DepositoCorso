# Uso di una tupla per salvare i nomi degli utenti 
utenti = (
    ("antonio", "1234"),
    ("mirko", "1234"),
    ("mario", "1234")
)
#Lista magazzino
magazzino = []
loggato = False
def mostra_messaggio(messaggio):
    def decoratore(funzione):
        def wrapper(*args, **kwargs):
            print(messaggio)
            return funzione()
        return wrapper
    return decoratore


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
# FUNZIONE DI AGGIUNTA PRODOTTO 
@mostra_messaggio("Aggiuta prodotto decoratore")
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
# FUNZIONE DI MOSTRA PRODOTTO        
@mostra_messaggio("Mostra prodotto decoratore")
def mostra_prodotti():
    if len(magazzino) == 0:
        print("Il magazzino è vuoto")
    else:
        print("Prodotti in magazzino:")
        for prodotto in magazzino:
            print("Nome: " + prodotto[0] + ", Quantita: " + str(prodotto[1]))
# FUNZIONE DI MOSTRA PRODOTTO NO DUPLICATI           
@mostra_messaggio("Mostra prodotto non duplicati decoratore")
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