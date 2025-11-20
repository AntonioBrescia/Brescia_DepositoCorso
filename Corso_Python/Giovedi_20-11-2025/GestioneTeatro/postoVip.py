from posto import Posto

class PostoVIP(Posto):
    def __init__(self, numero, fila, servizi_extra=None):
        super().__init__(numero, fila)
        self.__servizi_extra = servizi_extra if servizi_extra else []

    def prenota(self):
        if self.is_occupato():
            print(f"Il posto VIP {self.get_fila()}{self.get_numero()} è già occupato.")
        else:
            super().prenota()
            if self.__servizi_extra:
                print("Servizi extra attivati:")
                for s in self.__servizi_extra:
                    print(" -", s)