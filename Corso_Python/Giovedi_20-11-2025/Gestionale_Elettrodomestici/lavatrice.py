from elettrodomestico import Elettrodomestico

class Lavatrice(Elettrodomestico):
    def __init__(self, marca, modello, anno_acquisto, guasto, capacita_kg, giri_centrifuga):
        super().__init__(marca, modello, anno_acquisto, guasto)
        self.__capacita_kg = capacita_kg  # capacità in kg
        self.__giri_centrifuga = giri_centrifuga  # numero di giri centrifuga

    # Getter e setter
    def get_capacita_kg(self):
        return self.__capacita_kg

    def set_capacita_kg(self, capacita):
        self.__capacita_kg = capacita

    def get_giri_centrifuga(self):
        return self.__giri_centrifuga

    def set_giri_centrifuga(self, giri):
        self.__giri_centrifuga = giri

    # Override del metodo stima_costo_base
    def stima_costo_base(self):
        costo = super().stima_costo_base()  
        if self.__capacita_kg > 8:
            costo += 20  # maggiorazione per lavatrici grandi
        if self.__giri_centrifuga > 1200:
            costo += 15  # maggiorazione per centrifuga potente
        return costo
