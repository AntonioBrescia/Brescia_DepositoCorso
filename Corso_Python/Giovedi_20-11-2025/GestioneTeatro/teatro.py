class Teatro:
    def __init__(self):
        self.__posti = []

    def aggiungi_posto(self, posto):
        self.__posti.append(posto)

    def prenota_posto(self, numero, fila):
        for p in self.__posti:
            if p.get_numero() == numero and p.get_fila() == fila:
                p.prenota()
                return
        print("Posto non trovato.")

    def stampa_posti_occupati(self):
        print("\nPosti occupati:")
        trovati = False
        for p in self.__posti:
            if p.is_occupato():
                print(f"- {p.get_fila()}{p.get_numero()}")
                trovati = True
        if not trovati:
            print("Nessun posto occupato.")
