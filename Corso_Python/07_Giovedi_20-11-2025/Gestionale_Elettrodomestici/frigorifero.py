from elettrodomestico import Elettrodomestico
 
class Frigorifero(Elettrodomestico):
    def __init__(self, marca, modello, anno_acquisto, guasto, litri, ha_freezer):
        super().__init__(marca, modello, anno_acquisto, guasto)
        self.__litri = litri
        self.__ha_freezer = ha_freezer  

    # Getter e setter
    def get_litri(self):
        return self.__litri

    def set_litri(self, litri):
        self.__litri = litri

    def get_ha_freezer(self):
        return self.__ha_freezer

    def set_ha_freezer(self, freezer):
        self.__ha_freezer = freezer

    # Override del metodo stima_costo_base
    def stima_costo_base(self):
        costo = super().stima_costo_base()  # prendi il costo base dal padre
        if self.__litri > 200:
            costo += 25  # maggiorazione se è grande
        if self.__ha_freezer:
            costo += 20  # aggiunta per il freezer
        return costo
