from elettrodomestico import Elettrodomestico
from lavatrice import Lavatrice
from forno import Forno
from frigorifero import Frigorifero
from ticketRiparazione import TicketRiparazione
from officina import Officina

# Creiamo l'officina
officina = Officina("Officina1")

def crea_ticket():
    print("Seleziona tipo di elettrodomestico:")
    print("1. Lavatrice")
    print("2. Frigorifero")
    print("3. Forno")
    scelta = input("Scelta: ")
    
    marca = input("Marca: ")
    modello = input("Modello: ")
    anno = int(input("Anno acquisto: "))
    guasto = input("Guasto: ")

    if scelta == "1":
        capacita = int(input("Capacità kg: "))
        giri = int(input("Giri centrifuga: "))
        elettro = Lavatrice(marca, modello, anno, guasto, capacita, giri)
    elif scelta == "2":
        litri = int(input("Litri: "))
        freezer = input("Ha freezer? (s/n): ").lower() == 's'
        elettro = Frigorifero(marca, modello, anno, guasto, litri, freezer)
    elif scelta == "3":
        tipo = input("Tipo alimentazione (elettrico/gas): ").lower()
        ventilato = input("Ha funzione ventilata? (s/n): ").lower() == 's'
        elettro = Forno(marca, modello, anno, guasto, tipo, ventilato)
    else:
        print("Scelta non valida!")
        return

    id_ticket = len(officina.tickets) + 1
    ticket = TicketRiparazione(id_ticket, elettro)
    officina.aggiungi_ticket(ticket)
    print(f"Ticket {id_ticket} creato con successo!")

def menu():
    while True:
        print("\n--- MENU OFFICINA ---")
        print("1. Crea nuovo ticket")
        print("2. Chiudi ticket")
        print("3. Stampa ticket aperti")
        print("4. Totale preventivi")
        print("5. Statistiche per tipo")
        print("0. Esci")

        scelta = input("Seleziona un'opzione: ")

        match scelta:
            case "1":
                crea_ticket()
            case "2":
                officina.stampa_ticket_aperti()
                id_ticket = int(input("ID ticket da chiudere: "))
                if officina.chiudi_ticket(id_ticket):
                    print("Ticket chiuso.")
                else:
                    print("Ticket non trovato.")
            case "3":
                officina.stampa_ticket_aperti()
            case "4":
                totale = officina.totale_preventivi()
                print(f"Totale preventivi: {totale} €")
            case "5":
                officina.statistiche_per_tipo()
            case "0":
                print("Uscita dal programma.")
                break
            case _:
                print("Opzione non valida!")

if __name__ == "__main__":
    menu()
