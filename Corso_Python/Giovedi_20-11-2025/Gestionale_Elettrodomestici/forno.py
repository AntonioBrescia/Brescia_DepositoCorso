from elettrodomestico import Elettrodomestico
class Forno(Elettrodomestico):
    def __init__(self, marca, modello, anno_acquisto, guasto, tipo_alimentazione, ha_ventilato):
        super().__init__(marca, modello, anno_acquisto, guasto)
        self.__tipo_alimentazione = tipo_alimentazione  # "elettrico" o "gas"
        self.__ha_ventilato = ha_ventilato  # True/False

    # Getter e setter
    def get_tipo_alimentazione(self):
        return self.__tipo_alimentazione

    def set_tipo_alimentazione(self, tipo):
        self.__tipo_alimentazione = tipo

    def get_ha_ventilato(self):
        return self.__ha_ventilato

    def set_ha_ventilato(self, ventilato):
        self.__ha_ventilato = ventilato

    # Override del metodo stima_costo_base
    def stima_costo_base(self):
        costo = super().stima_costo_base() 
        if self.__tipo_alimentazione == "elettrico":
            costo += 20
        elif self.__tipo_alimentazione == "gas":
            costo += 30
        if self.__ha_ventilato:
            costo += 15
        return costo
   
    