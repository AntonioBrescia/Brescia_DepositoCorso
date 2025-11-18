from membroSquadra import MembroSquadra 
import random


class Giocatore(MembroSquadra): 
    def __init__(self, nome, eta, ruolo, numero_maglia):
        self.nome = nome
        self.eta = eta 
        self.ruolo = ruolo
        self.numero_maglia = numero_maglia
    
    def gioca_partita(self):
        numero_casuale = random.randint(1, 10)
        print(f"Complimenti {self.nome} hai fatto {numero_casuale} goal")