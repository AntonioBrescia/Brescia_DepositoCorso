class Computer:

    def __init__(self):
        self.__processore = "Intel i5"  # Attributo privato

    def get_processore(self):
        return self.__processore

    def set_processore(self, processore):
        self.__processore = processore

    # Metodo privato
    def __mostra_info_privata(self):
        print(f"Informazioni riservate: processore = {self.__processore}")


    # Metodo pubblico per chiamare il metodo privato dall'esterno
    def mostra_info(self):
        self.__mostra_info_privata()


# Test classe Computer
pc = Computer()
print(pc.get_processore())  # Accesso tramite getter

pc.set_processore("AMD Ryzen 5")  # Modifica tramite setter
print(pc.get_processore())

# Chiamata al metodo privato tramite metodo pubblico
pc.mostra_info()  # Output: Informazioni riservate: processore = AMD Ryzen 5


# --- Esempio variabili globale, locale e nonlocal ---

# Variabile globale
numero = 10

def funzione_esterna():
    # Variabile locale nella funzione esterna
    numero = 5
    print("Numero dentro funzione_esterna (locale):", numero)    

    def funzione_interna():
        # Utilizzo nonlocal per modificare la variabile locale della funzione esterna
        nonlocal numero
        numero = 3
        print("Numero dentro funzione_interna (nonlocal):", numero)

    funzione_interna()
    print("Numero dentro funzione_esterna dopo interna:", numero)

print("Numero nel main (globale):", numero)
funzione_esterna()
print("Numero nel main dopo chiamata (globale non cambiato):", numero)


# PROTETTE 

class ClasseBase:
    def __init__(self):
        self._variabile_protetta = "Sono protetta"

class SottoClasse(ClasseBase):
    def __init__(self):
        super().__init__()
        print(self._variabile_protetta) # Accesso consentito

obj = SottoClasse()
    # Accesso da fuori la classe (non consigliato, ma possibile)
print(obj._variabile_protetta)
