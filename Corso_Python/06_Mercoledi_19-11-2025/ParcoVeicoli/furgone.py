from veicolo import Veicolo

class Furgone(Veicolo):
    def __init__(self, marca, modello, anno, capacita_carico):
        super().__init__(marca, modello, anno)
        self.__capacita_carico = capacita_carico
        self.__carico_attuale = 0

    def carica(self, quantita):
        if self.__carico_attuale + quantita <= self.__capacita_carico:
            self.__carico_attuale += quantita
            print(f"Caricati {quantita} kg. Carico attuale: {self.__carico_attuale} kg.")
        else:
            print("Superata capacità massima!")

    def scarica(self, quantita):
        if quantita <= self.__carico_attuale:
            self.__carico_attuale -= quantita
            print(f"Scaricati {quantita} kg. Carico residuo: {self.__carico_attuale} kg.")
        else:
            print("Non c'è abbastanza carico da scaricare!")

    def __str__(self):
        return super().__str__() + f" | Carico: {self.__carico_attuale}/{self.__capacita_carico} kg"
