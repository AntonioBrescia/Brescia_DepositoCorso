from abc import ABC, abstractmethod

class VeicoloTrasporto(ABC):
    def __init__(self, targa: str, peso_massimo: int):
        self._targa = targa
        self._peso_massimo = peso_massimo
        self._carico_attuale = 0

        
    def carica(self, peso: int):
        if self._carico_attuale + peso <= self._peso_massimo:
            self._carico_attuale += peso
            print(f"Caricati {peso} kg sul veicolo")
        else:
            print(f"non è possibile caricare {peso} kg perchè supera la capacità massima")
            

    def scarica(self):
        print(f"Scaricato veicolo {self._targa}.")
        self._carico_attuale = 0

    @abstractmethod
    def costo_manutenzione(self):
        pass