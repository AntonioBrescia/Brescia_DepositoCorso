class Veicolo:
    def __init__(self, marca, modello, anno):
        self.__marca = marca
        self.__modello = modello
        self.__anno = anno
        self.__accensione = False

    def accendi(self):
        if not self.__accensione:
            self.__accensione = True
            print(f"il veicolo {self.__marca} {self.__modello} è acceso.")
        else:
            print(f"il veicolo {self.__marca} {self.__modello} è già acceso.")

    def spegni(self): 
        if self.__accensione:
            self.__accensione = False
            print(f"il veicolo {self.__marca} {self.__modello} è spento.")
        else:
            print(f"il veicolo {self.__marca} {self.__modello} è già spento.")

    def __str__(self):
        stato = "Acceso" if self.__accensione else "Spento"
        return f"{self.__marca} {self.__modello} ({self.__anno}) - {stato}"
