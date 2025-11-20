from veicolo import Veicolo

class Auto(Veicolo):
    def __init__(self, marca, modello, anno, numero_porte):
        super().__init__(marca, modello, anno)
        self.__numero_porte = numero_porte

    def suona_clacson(self):
        print("HO SUANATOO")
    
    def __str__(self):
        return super().__str__() + f" | Porte: {self.__numero_porte}"
