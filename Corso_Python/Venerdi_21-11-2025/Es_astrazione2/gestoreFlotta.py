class GestoreFlotta:
    def __init__(self):
        self.veicoli = []

    def aggiungi_veicolo(self, veicolo):
        self.veicoli.append(veicolo)
        print(f"Veicolo {veicolo._targa} aggiunto.")

    def rimuovi_veicolo(self, targa):
        for v in self.veicoli:
            if v._targa == targa:
                self.veicoli.remove(v)
                print(f"Veicolo {targa} rimosso.")
                return
        print(f"Nessun veicolo con targa {targa} trovato.")

    def costo_totale_manutenzione(self):
        return sum(v.costo_manutenzione() for v in self.veicoli)

    def stampa_veicoli(self):
        print("--- Veicoli ---")
        for v in self.veicoli:
            print(f"{v._targa} | {v.tipo} | Carico: {v._carico_attuale} kg")
        print("-------------------------")
