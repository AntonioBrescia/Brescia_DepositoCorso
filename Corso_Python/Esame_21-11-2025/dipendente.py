from persona import Persona

class Dipendente(Persona):
    def __init__(self, nome, cognome, ruolo, badge):
        super().__init__(nome, cognome)
        self.__ruolo = ruolo
        self.badge = badge
        self.stato = "fuori" 

    @property
    def ruolo(self):
        return self.__ruolo.nome

    def __str__(self):
        return f"{self.nome} {self.cognome} , {self.ruolo} (Badge: {self.badge.codice})"
