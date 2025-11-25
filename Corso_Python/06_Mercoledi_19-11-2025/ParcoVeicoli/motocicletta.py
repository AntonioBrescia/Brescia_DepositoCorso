from veicolo import Veicolo

class Motocicletta(Veicolo):
    def __init__(self, marca, modello, anno, tipo):
        super().__init__(marca, modello, anno)
        self.__tipo = tipo

    def esegui_wheelie(self):
        if self.__tipo.lower() == "sportiva":
            print("La motocicletta impenna")
        else:
            print("Questa motocicletta non impenna.")

    def __str__(self):
        return super().__str__() + f" | Tipo: {self.__tipo}"
