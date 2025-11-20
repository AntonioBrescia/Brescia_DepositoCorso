from lavatrice import Lavatrice
from frigorifero import Frigorifero
from forno import Forno

class Officina:
    def __init__(self, nome):
        self.nome = nome
        self.tickets = []  # lista di oggetti TicketRiparazione

    def aggiungi_ticket(self, ticket):
        self.tickets.append(ticket)

    def chiudi_ticket(self, id_ticket):
        for ticket in self.tickets:
            if ticket.get_id_ticket() == id_ticket:
                ticket.set_stato("chiuso")
                return True
        return False

    def stampa_ticket_aperti(self):
        for ticket in self.tickets:
            if ticket.get_stato() != "chiuso":
                elettro = ticket.get_elettrodomestico()
                print(f"ID: {ticket.get_id_ticket()} | Tipo: {type(elettro).__name__} | Stato: {ticket.get_stato()}")

    def totale_preventivi(self):
        totale = 0
        for ticket in self.tickets:
            totale += ticket.calcola_preventivo()
        return totale

    def statistiche_per_tipo(self):
        num_lavatrici = 0
        num_frigoriferi = 0
        num_forni = 0

        for ticket in self.tickets:
            elettro = ticket.get_elettrodomestico()
            if isinstance(elettro, Lavatrice):
                num_lavatrici += 1
            elif isinstance(elettro, Frigorifero):
                num_frigoriferi += 1
            elif isinstance(elettro, Forno):
                num_forni += 1

        print(f"Numero di lavatrici in riparazione: {num_lavatrici}")
        print(f"Numero di frigoriferi in riparazione: {num_frigoriferi}")
        print(f"Numero di forni in riparazione: {num_forni}")
