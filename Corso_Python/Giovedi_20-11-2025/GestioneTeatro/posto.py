class Posto:
    def __init__(self, numero: int, fila: str):
        self.__numero = numero
        self.__fila = fila
        self.__occupato = False   

        
    def get_numero(self):
        return self.__numero

    def get_fila(self):
        return self.__fila

    def is_occupato(self):
        return self.__occupato

    def prenota(self):
        if self.__occupato:
            print(f"Il posto {self.__fila}{self.__numero} è già occupato.")
        else:
            self.__occupato = True
            print(f"Posto {self.__fila}{self.__numero} prenotato correttamente.")

    def libera(self):
        if not self.__occupato:
            print(f"Il posto {self.__fila}{self.__numero} non era prenotato.")
        else:
            self.__occupato = False
            print(f"Posto {self.__fila}{self.__numero} liberato correttamente.")

    def __str__(self):
        stato = "Occupato" if self.__occupato else "Libero"
        return f"Posto {self.__fila}{self.__numero} - {stato}"