class Elettrodomestico:
    def __init__(self, marca, modello, anno_acquisto, guasto):
        # attributi privati
        self.__marca = marca
        self.__modello = modello
        self.__anno_acquisto = anno_acquisto
        self.__guasto = guasto

    # Getter e Setter
    def get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        self.__marca = marca

    def get_modello(self):
        return self.__modello

    def set_modello(self, modello):
        self.__modello = modello

    def get_anno_acquisto(self):
        return self.__anno_acquisto

    def set_anno_acquisto(self, anno):
        self.__anno_acquisto = anno

    def get_guasto(self):
        return self.__guasto

    def set_guasto(self, guasto):
        self.__guasto = guasto

    def descrizione(self):
        return f"{self.__marca} {self.__modello} ({self.__anno_acquisto}) - Guasto: {self.__guasto}"

    def stima_costo_base(self):
        return 50  
