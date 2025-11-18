from membroSquadra import MembroSquadra

class Assistente(MembroSquadra): 
    def __init__(self, nome, eta, specializzazione):
        super().__init__(nome, eta)  
        self.specializzazione = specializzazione
    
    def supporta_team(self):
        print(f"{self.nome} sta supportando il team con la specializzazione in {self.specializzazione}.")
