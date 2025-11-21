from datetime import datetime

class Accesso:
    def __init__(self):
        self.log = []  # lista di tuple (dipendente, tipo, timestamp)

    def entra(self, dipendente):
        # Controllo badge attivo
        if not dipendente.badge.attivo:
            print(f"Accesso negato: badge {dipendente.badge.codice} non attivo per {dipendente}")
            return

        # se dipendente è già “dentro” non può timbrare entrata di nuovo
        if dipendente.stato == "dentro":
            print(f"{dipendente} ha già timbrato l’entrata.")
            return

        now = datetime.now()
        self.log.append((dipendente, "entrata", now))
        dipendente.stato = "dentro"
        print(f"Entrata registrata per {dipendente} alle {now}")

    def esci(self, dipendente):
        # se il dipendente è fuori, non può uscire
        if dipendente.stato != "dentro":
            print(f"{dipendente} non risulta dentro, impossibile registrare uscita.")
            return

        now = datetime.now()
        self.log.append((dipendente, "uscita", now))
        dipendente.stato = "fuori"
        print(f"Uscita registrata per {dipendente} alle {now}")

    def mostra_log(self):
        if not self.log:
            print("Nessun evento registrato.")
            return

        print("Log accessi:")
        for (dip, tipo, time) in self.log:
            print(f"{dip} — {tipo} — {time}")
