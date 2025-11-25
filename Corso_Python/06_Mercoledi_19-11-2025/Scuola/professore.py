from persona import Persona
from studente import Studente

class Professore(Persona):
    def __init__(self, nome, eta, materia):
        super().__init__(nome, eta)
        self.__materia = materia

    def get_materia(self):
        return self.__materia

    def set_materia(self, materia):
        if materia.strip() != "":
            self.__materia = materia.strip()
        else:
            print("Materia non valida.")

    def inserisci_voto(self, studente, voto):
        studente.aggiungi_voto(voto)
        print("Voto", voto, "inserito per lo studente", studente.get_nome())

    def presentazione(self):
        print("Ciao, mi chiamo", self.get_nome(), "ho", self.get_eta(), "anni e insegno", self.__materia)
