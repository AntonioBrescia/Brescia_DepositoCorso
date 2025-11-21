class Ruolo:
    ruoli_disponibili = []

    def __init__(self, nome):
        self.nome = nome
        Ruolo.ruoli_disponibili.append(self)

# Funzione per mostrare i ruoli
def mostra_ruoli():
    if Ruolo.ruoli_disponibili:
        print("Ruoli disponibili:")
        for ruolo in Ruolo.ruoli_disponibili:
            print("-", ruolo.nome)
    else:
        print("Nessun ruolo disponibile.")

# Funzione per trovare un ruolo per nome
def trova_ruolo(nome):
    for ruolo in Ruolo.ruoli_disponibili:
        if ruolo.nome.lower() == nome.lower():
            return ruolo
    return None
