class GestoreParcoVeicoli:
    def __init__(self):
        self.__veicoli = []

    def aggiungi_veicolo(self, veicolo):
        self.__veicoli.append(veicolo)

    def cerca_veicolo(self, marca, modello):
        for v in self.__veicoli:
            if v.marca == marca and v.modello == modello:
                return v
        return None

    @property
    def veicoli(self):
        return self.__veicoli.copy()  # restituisce copia per protezione
