from dipendente import Dipendente
from accesso import Accesso
from ruolo import Ruolo, mostra_ruoli, trova_ruolo
from badge import Badge
import random

#inizzializzo un insieme per i badge, una lista di dipendenti e il gestore (oggetto della classe accesso) 
badge_assegnati = set()
dipendenti = []
gestore = Accesso()

# Creo ruoli di esempio 
Ruolo("Dipendente")
Ruolo("Manager")
Ruolo("Direttore")

# Funzione per creare budge univoco con il modulo random 
def genera_codice_badge():
    while True:
        codice = f"{random.randint(100, 999)}"
        if codice not in badge_assegnati:
            badge_assegnati.add(codice)
            return codice

# funzione per il menu 
def mostra_menu():
    print("--- Gestionale Lavoro ---")
    print("1. Aggiungi dipendente")
    print("2. Registra entrata dipendente")
    print("3. Registra uscita dipendente")
    print("4. Mostra log accessi")
    print("5. Disattiva badge dipendente")
    print("6. Mostra ruoli disponibili")
    print("7. Esci")
    return input("Seleziona un'opzione: ")

#funzione per trovare il dipendente tramite il nome 
def trova_dipendente(nome):
    for d in dipendenti:
        if d.nome.lower() == nome.lower():
            return d
    return None

# Ciclo padre
while True:
    #Rchiamo la funziona per il  menu 
    scelta = mostra_menu()

# tramite un match gestisco le scelte 
    match scelta:
        case "1":
            nome = input("Nome: ")
            cognome = input("Cognome: ")
            #chiamo la funzione dal modulo ruolo 
            mostra_ruoli()
            nome_ruolo = input("Seleziona il ruolo tramite il nome: ")
            ruolo = trova_ruolo(nome_ruolo)
            if not ruolo:
                print("Ruolo non trovato. Dipendente non aggiunto.")
                #torno al menu se il ruolo non esiste 
                continue
            #genero il budge randomico e creo un oggetto budge 
            codice_badge = genera_codice_badge()
            badge = Badge(codice_badge)
            #creo il dipendente passando nome e cognome l'oggetto ruolo e l'oggetto badge 
            d = Dipendente(nome, cognome, ruolo, badge)
            dipendenti.append(d)
            #aggiungo alla lista 
            print(f"Dipendente aggiunto: {d}")

        case "2":
            #ingresso del dipendente
            nome = input("Nome del dipendente: ")
            d = trova_dipendente(nome)
            if d:
                gestore.entra(d)
            else:
                print("Dipendente non trovato!")

        case "3":
            #uscita del dipendente
            #trova dip mi restituisce true o false, se true permetto l'uscita 
            nome = input("Nome del dipendente: ")
            d = trova_dipendente(nome)
            if d:
                #controllo in esci se è fuori o dentro 
                gestore.esci(d)
            else:
                print("Dipendente non trovato!")

        case "4":
            #mostro tutti i dipendenti con dip , ruolo e time 
            gestore.mostra_log()

        case "5":
            nome = input("Nome del dipendente da disattivare badge: ")
            d = trova_dipendente(nome)
            #se trovo il dipendende posso richiamre la funzione disattiva e stampo un mess
            if d:
                d.badge.disattiva()
                print(f"Badge {d.badge.codice} disattivato per {d}")
            else:
                print("Dipendente non trovato")

        case "6":
            #chiamo alla funzione mostra ruoli tramite un for itero sugli elementi 
            mostra_ruoli()

        case "7":
            #uscita 
            print("Arrivederci")
            break

        case _:
            print("Opzione non valida, riprova.")
