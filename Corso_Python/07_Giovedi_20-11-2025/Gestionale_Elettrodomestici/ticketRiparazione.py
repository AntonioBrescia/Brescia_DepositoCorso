class TicketRiparazione:
    def __init__(self, id_ticket, elettrodomestico):
        self.__id_ticket = id_ticket
        self.__elettrodomestico = elettrodomestico  
        self.__stato = "aperto"  
        self.__note = []  

    # Getter e setter
    def get_id_ticket(self):
        return self.__id_ticket

    def get_elettrodomestico(self):
        return self.__elettrodomestico

    def get_stato(self):
        return self.__stato

    def set_stato(self, stato):
        if stato in ["aperto", "in lavorazione", "chiuso"]:
            self.__stato = stato
        else:
            print("Stato non valido.")

    def get_note(self):
        return self.__note

    # Aggiunge una nota al ticket
    def aggiungi_nota(self, testo):
        self.__note.append(testo)

    # Metodo variadico per calcolare il preventivo
    def calcola_preventivo(self, *voci_extra):
        costo = self.__elettrodomestico.stima_costo_base()  # polimorfismo
        costo += sum(voci_extra)  # somma tutte le voci extra passate
        return costo
