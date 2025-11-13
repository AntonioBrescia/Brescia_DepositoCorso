#Es registrazione
print("Benvenuto nella pagina di registrazione!")
#Creazione liste per memorizzare nomi utente e password
nomi_utenti = []        
password = []
#Input da parte dell'utente
nuovo_nome_utente = input("Inserisci un nuovo nome utente: ")   
nuova_password = input("Inserisci una nuova password: ")
#Aggiunta del nuovo nome utente e password alle liste
nomi_utenti.append(nuovo_nome_utente)   
password.append(nuova_password)
print("Registrazione avvenuta con successo!")   
print("Nomi utente registrati:", nomi_utenti)
print("Password registrate:", password)
