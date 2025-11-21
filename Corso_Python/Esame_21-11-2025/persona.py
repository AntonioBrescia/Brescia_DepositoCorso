from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nome, cognome):
        self.__nome = nome
        self.__cognome = cognome

    @property
    def nome(self):
        return self.__nome

    @property
    def cognome(self):
        return self.__cognome

    @abstractmethod
    def ruolo(self):
        pass
