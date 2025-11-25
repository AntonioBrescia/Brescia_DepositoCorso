from posto import Posto


class PostoStandard(Posto):
    def __init__(self, numero, fila, costo: float):
        super().__init__(numero, fila)
        self.__costo = costo

    def prenota(self):
        if self.is_occupato():
            print(f"Il posto Standard {self.get_fila()}{self.get_numero()} è già occupato.")
        else:
            super().prenota()
            print(f"Costo della prenotazione: {self.__costo}€")