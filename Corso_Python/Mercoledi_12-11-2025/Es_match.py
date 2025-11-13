# Esercizio Sistema di login

print("Benvenuto nella pagina di registrazione!")

# Liste per memorizzare nomi utente e password
nomi_utenti = []        
passwords = []

# Input da parte dell'utente
nuovo_nome_utente = input("Inserisci un nuovo nome utente: ")
nuova_password = input("Inserisci una nuova password: ")

# Aggiunta del nuovo nome utente e password alle liste
nomi_utenti.append(nuovo_nome_utente)
passwords.append(nuova_password)

print("Registrazione avvenuta con successo!")
print("Nomi utente registrati:", nomi_utenti)
print("Password registrate:", passwords)

# --- LOGIN ---
nome_utente_corretta = nomi_utenti[0]
password_corretta = passwords[0]

# Input da parte dell'utente
nome_utente = input("Inserisci il nome utente: ")
password_inserita = input("Inserisci la password: ")

# Verifica delle credenziali
if nome_utente == nome_utente_corretta and password_inserita == password_corretta:
    print("Benvenuto " + nome_utente + "!")
    print("Scegli una delle seguenti domande:")
    print("1. Qual è il tuo colore preferito?")
    print("2. Qual è il tuo animale preferito?")

    scelta = input("Scegli 1 o 2: ")

    # Struttura match per gestire la scelta
    match scelta:
        case "1":
            colore = input("Inserisci il tuo colore preferito: ")
            print("Hai scelto il:", colore)
        case "2":
            animale = input("Inserisci il tuo animale preferito: ")
            print("Hai scelto:", animale)
        case _:
            print("Scelta non valida.")
else:
    print("Nome utente o password errati. Accesso negato.")
