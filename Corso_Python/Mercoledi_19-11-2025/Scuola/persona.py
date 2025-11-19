class Persona:
    def __init__(self, nome, eta):
        self.__nome = nome
        self.__eta = eta

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        if nome.strip() != "" and nome.replace(" ", "").isalpha():
            self.__nome = nome.strip()
        else:
            print("Nome non valido.")

    def get_eta(self):
        return self.__eta

    def set_eta(self, eta):
        if eta > 0:
            self.__eta = eta
        else:
            print("Età non valida.")

    def presentazione(self):
        print("Ciao, mi chiamo", self.__nome, "e ho", self.__eta, "anni.")
