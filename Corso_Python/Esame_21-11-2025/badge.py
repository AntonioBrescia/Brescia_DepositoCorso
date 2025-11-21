from datetime import datetime

class Badge:
    def __init__(self, codice):
        self.__codice = codice
        self.__attivo = True
        self.__ultimo_accesso = None

    @property
    def codice(self):
        return self.__codice

    @property
    def ultimo_accesso(self):
        return self.__ultimo_accesso

    @property
    def attivo(self):
        return self.__attivo

    def registra_accesso(self):
        if self.__attivo:
            self.__ultimo_accesso = datetime.now()
            return True
        return False

    def disattiva(self):
        self.__attivo = False
