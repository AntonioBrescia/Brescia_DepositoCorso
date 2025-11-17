class Ristorante:
    def __init__(self, nome, tipoCucina):
        self.nome = nome
        self.tipoCucina = tipoCucina
        self.aperto = False
        self.menu = {}
        
    def descrivi_ristorante(self):
        print(f"Il ristorante {self.nome} offre cucina {self.tipoCucina}")
        
    def stato_apertura(self):
        if(self.aperto == False):
            print("ristorante chiuso")
        else:
            print("ristorante aperto")

        
    def apri_ristorante(self):
        self.aperto = True
        print("Il ristorante è ora aperto.")
        
    def chiudi_ristorante(self):
        self.aperto = False
        print("Il ristorante è ora chiuso.")
        
    def aggiungi_al_menu(self, piatto, prezzo):
        self.menu[piatto] = prezzo
        print(f"Piatto '{piatto}' aggiunto al menu.")

    def togli_dal_menu(self, piatto):
        if piatto in self.menu:
            self.menu.pop(piatto)
            print(f"Piatto '{piatto}' rimosso dal menu.")
        else:
            print("Piatto non presente nel menu.")
        
    def stampa_menu(self):
        if len(self.menu) == 0:
            print("Il menu è vuoto.")
            return
        print("\n--- MENU DEL RISTORANTE ---")
        for piatto, prezzo in self.menu.items():
            print(f"- {piatto}: {prezzo}€")
        print("-----------------------------\n")

nomeRistorante = input("Come si chiama il Ristorante?")
tipoCucina = input("Che tipo di cucina offri?")
ristorante1 = Ristorante(nomeRistorante, tipoCucina)

while True:
    print("""
        --- MENU PRINCIPALE ---
        1. Descrivi il ristorante
        2. Controlla stato apertura
        3. Apri ristorante
        4. Chiudi ristorante
        5. Aggiungi piatto al menu
        6. Rimuovi piatto dal menu
        7. Stampa menu
        0. Esci
        """)
    scelta = input("Scegli un opzione: ")
    match scelta:
        case "1":
            ristorante1.descrivi_ristorante()

        case "2":
            ristorante1.stato_apertura()

        case "3":
            ristorante1.apri_ristorante()

        case "4":
            ristorante1.chiudi_ristorante()

        case "5":
            piatto = input("Nome del piatto: ")
            prezzo = float(input("Prezzo del piatto: "))
            ristorante1.aggiungi_al_menu(piatto, prezzo)

        case "6":
            piatto = input("Nome del piatto da rimuovere: ")
            ristorante1.togli_dal_menu(piatto)

        case "7":
            ristorante1.stampa_menu()

        case "0":
            print("Arrivederci")
            break

        case _:
            print("Scelta non valida!")

#dizionario con all'interno i valori dell'oggetto 