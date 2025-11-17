class Penna:
    numero_penna = 0  # attributo di classe condiviso

    def __init__(self, colore, materiale):
        self.colore = colore       # attributo dell'istanza
        self.materiale = materiale
        Penna.numero_penna += 1    # aggiorna l'attributo di classe

    # -------------------------
    # Metodo di istanza
    # -------------------------
    def cambia_colore(self, nuovo_colore):
        """Modifica il colore di questa penna."""
        self.colore = nuovo_colore

    # -------------------------
    # Metodo di classe
    # -------------------------
    @classmethod
    def quante_penne(cls):
        """Restituisce quante penne sono state create."""
        return cls.numero_penna

    # -------------------------
    # Metodo statico
    # -------------------------
    @staticmethod
    def materiale_valido(materiale):
        """Verifica se il materiale è valido per una penna."""
        return materiale.lower() in ["plastica", "metallo", "legno"]


# --- Esempio di utilizzo ---

# Creazione di due oggetti Penna
p1 = Penna("rosso", "plastica")
p2 = Penna("blu", "vetro")

# Metodo di istanza: agisce su un oggetto specifico
p1.cambia_colore("verde")
print(p1.colore)  # verde
print(p2.colore)  # blu

# Metodo di classe: agisce sulla classe
print(Penna.quante_penne())  # 2

# Metodo statico: non dipende né dall'oggetto né dalla classe
print(Penna.materiale_valido("plastica"))  # True
print(Penna.materiale_valido("vetro"))     # False
