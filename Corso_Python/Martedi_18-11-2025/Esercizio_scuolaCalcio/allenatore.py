from membroSquadra import MembroSquadra

class Allenatore(MembroSquadra): 
    def __init__(self, nome, eta, anni_esperienza):
        super().__init__(nome, eta)  
        self.anni_esperienza = anni_esperienza
    
    def dirige_allenamento(self):
        print(f"{self.nome} sta dirigendo l'allenamento con {self.anni_esperienza} anni di esperienza.")
