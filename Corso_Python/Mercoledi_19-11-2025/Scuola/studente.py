from persona import Persona

class Studente(Persona):
    def __init__(self, nome, eta):
        super().__init__(nome, eta)
        self.__voti = []

    def get_voti(self):
        return self.__voti

    def aggiungi_voto(self, voto):
        if voto >= 0 and voto <= 10:
            self.__voti.append(voto)
        else:
            print("Voto non valido (0-10).")

    def calcola_media(self):
        if len(self.__voti) == 0:
            return 0
        return sum(self.__voti) / len(self.__voti)

    def presentazione(self):
        media = self.calcola_media()
        print("Ciao, mi chiamo", self.get_nome(), "ho", self.get_eta(), "anni e la mia media è", media)
