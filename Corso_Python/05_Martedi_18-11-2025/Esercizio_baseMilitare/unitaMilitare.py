import random  # Per generare numeri casuali, usati negli attacchi
import time    # Per aggiungere pause tra i turni, rendendo il gioco più realistico

# ==========================
# CLASSI BASE
# ==========================

class UnitaMilitare:
    """
    Classe base per tutte le unità militari.
    Attributi:
        - nome: nome dell'unità
        - numero_soldati: numero di soldati presenti nell'unità
    Metodi:
        - muovi(): stampa un messaggio sul movimento
        - attacca(avversario): riduce i soldati dell'avversario
        - ritira(): stampa un messaggio di ritiro
        - __str__(): mostra informazioni sull'unità
    """
    def __init__(self, nome, numero_soldati):
        self.nome = nome
        self.numero_soldati = numero_soldati  # Imposta il numero iniziale di soldati

    def muovi(self):
        # Simula lo spostamento dell'unità
        print(f"{self.nome} si sta muovendo.")

    def attacca(self, avversario):
        # Genera un danno casuale tra 5 e 20 soldati
        danno = random.randint(5, 20)
        avversario.numero_soldati -= danno  # Riduce i soldati dell'avversario
        if avversario.numero_soldati < 0:  # Non permettere numeri negativi
            avversario.numero_soldati = 0
        print(f"{self.nome} attacca causando {danno} danni!")

    def ritira(self):
        # Messaggio per simulare un ritiro strategico
        print(f"{self.nome} si ritira temporaneamente per riorganizzarsi.")

    def __str__(self):
        # Rappresentazione testuale dell'unità per stampe semplici
        return f"{self.nome} - Soldati rimasti: {self.numero_soldati}"


# ==========================
# CLASSI DERIVATE (UNITÀ SPECIALIZZATE)
# ==========================

class Fanteria(UnitaMilitare):
    # Unità Fanteria, eredita tutto da UnitaMilitare
    def costruisci_trincea(self):
        # Azione speciale della Fanteria: aumenta la difesa
        print(f"{self.nome} costruisce una trincea aumentando la difesa!")
        self.numero_soldati += 5  # Guadagna 5 soldati extra

class Artiglieria(UnitaMilitare):
    # Unità Artiglieria
    def calibra_artiglieria(self):
        print(f"{self.nome} calibra l'artiglieria aumentando il danno al prossimo attacco!")
        self.numero_soldati += 3  # Guadagna 3 soldati extra

class Cavalleria(UnitaMilitare):
    # Unità Cavalleria
    def esplora_terreno(self):
        print(f"{self.nome} esplora il terreno e ottiene un vantaggio!")
        self.numero_soldati += 4

class SupportoLogistico(UnitaMilitare):
    # Unità Supporto Logistico
    def rifornisci_unita(self):
        print(f"{self.nome} effettua rifornimenti!")
        self.numero_soldati += 6

class Ricognizione(UnitaMilitare):
    # Unità Ricognizione
    def conduci_ricognizione(self):
        print(f"{self.nome} esegue una ricognizione, anticipando le mosse nemiche!")
        self.numero_soldati += 4


# ==========================
# CONTROLLO MILITARE
# ==========================

class ControlloMilitare(
    Fanteria, Artiglieria, Cavalleria, SupportoLogistico, Ricognizione
):
    """
    Classe che eredita tutte le unità specializzate per poter registrare e
    gestire facilmente le unità create.
    Attributi:
        - unita_registrate: dizionario con due liste separate per 'giocatore' e 'pc'
    Metodi:
        - registra_unita(unita, tipo): registra un'unità nella lista corretta
        - mostra_unita(): stampa tutte le unità registrate
        - dettagli_unita(nome): stampa i dettagli di una unità specifica
    """
    def __init__(self):
        self.unita_registrate = {"giocatore": [], "pc": []}  # Inizializza registro

    def registra_unita(self, unita, tipo="giocatore"):
        # Aggiunge l'unità alla lista corretta
        if tipo in self.unita_registrate:
            self.unita_registrate[tipo].append(unita)

    def mostra_unita(self):
        # Mostra tutte le unità registrate
        print("--- UNITÀ GIOCATORE ---")
        for u in self.unita_registrate["giocatore"]:
            print(u)
        print("--- UNITÀ PC ---")
        for u in self.unita_registrate["pc"]:
            print(u)

    def dettagli_unita(self, nome):
        # Cerca un'unità per nome e stampa i dettagli
        for tipo in self.unita_registrate:
            for u in self.unita_registrate[tipo]:
                if u.nome == nome:
                    print(f"\nDettagli dell'unità {nome}:")
                    print(u)
                    return
        print(f" Nessuna unità trovata con il nome {nome}")


# ==========================
# FUNZIONI DI GIOCO
# ==========================

def scegli_unita_giocatore():
    """
    Permette al giocatore di scegliere un'unità tra le cinque disponibili.
    Restituisce un'istanza della classe scelta con 100 soldati.
    """
    print("\nScegli la tua unità:")
    print("1 - Fanteria")
    print("2 - Artiglieria")
    print("3 - Cavalleria")
    print("4 - Supporto Logistico")
    print("5 - Ricognizione")
    
    scelta = input("Inserisci il numero: ")

    # Crea l'unità scelta
    if scelta == "1":
        return Fanteria("Fanteria", 100)
    if scelta == "2":
        return Artiglieria("Artiglieria", 100)
    if scelta == "3":
        return Cavalleria("Cavalleria", 100)
    if scelta == "4":
        return SupportoLogistico("Supporto Logistico", 100)
    if scelta == "5":
        return Ricognizione("Ricognizione", 100)

    # Se input non valido, riprova
    print("Scelta non valida. Riprova.")
    return scegli_unita_giocatore()


def scegli_unita_pc():
    """
    Seleziona casualmente un'unità per il PC.
    """
    classi = [
        Fanteria("Fanteria avversario", 100),
        Artiglieria("Artiglieria avversario", 100),
        Cavalleria("Cavalleria avversario", 100),
        SupportoLogistico("Supporto Logistico avversario", 100),
        Ricognizione("Ricognizione avversario", 100)
    ]
    return random.choice(classi)


def usa_abilita_speciale(unita):
    """
    Permette di usare l'abilità speciale dell'unità scelta.
    Controlla il tipo di unità e chiama il metodo corrispondente.
    """
    if isinstance(unita, Fanteria):
        unita.costruisci_trincea()
    elif isinstance(unita, Artiglieria):
        unita.calibra_artiglieria()
    elif isinstance(unita, Cavalleria):
        unita.esplora_terreno()
    elif isinstance(unita, SupportoLogistico):
        unita.rifornisci_unita()
    elif isinstance(unita, Ricognizione):
        unita.conduci_ricognizione()


def turno_giocatore(giocatore, pc):
    """
    Gestisce il turno del giocatore.
    Permette di scegliere tra attacco, movimento, ritiro o altre opzioni.
    """
    print("\n--- TUO TURNO ---")
    print("1 - Attacca")
    print("2 - Muoviti")
    print("3 - Ritirati")
    print("4 - Abilità speciale")
    print("5 - Mostra unità")
    print("6 - Dettagli unità")

    scelta = input("Inserisci il numero: ")

    if scelta == "1":
        giocatore.attacca(pc)
    elif scelta == "2":
        giocatore.muovi()
    elif scelta == "3":
        giocatore.ritira()
    elif scelta == "4":
        usa_abilita_speciale(giocatore)
    elif scelta == "5":
        controllo.mostra_unita()
    elif scelta == "6":
        nome = input("Inserisci il nome dell'unità: ")
        controllo.dettagli_unita(nome)
    else:
        print("Scelta non valida!")
        return turno_giocatore(giocatore, pc)  # Ripeti il turno se input errato


def turno_pc(pc, giocatore):
    """
    Gestisce il turno del PC.
    Il PC attacca automaticamente il giocatore.
    """
    print("\n--- TURNO DEL PC ---")
    time.sleep(1)  # Pausa di 1 secondo per simulare il tempo del turno
    pc.attacca(giocatore)


def gioco():
    """
    Funzione principale del gioco.
    - Seleziona le unità del giocatore e del PC
    - Registra le unità nel controllo militare
    - Esegue 3 round di combattimento
    - Determina il vincitore finale
    """
    giocatore = scegli_unita_giocatore()
    pc = scegli_unita_pc()

    # Registra le unità
    controllo.registra_unita(giocatore, "giocatore")
    controllo.registra_unita(pc, "pc")

    print(f"\nHai scelto: {giocatore.nome}")
    print(f"Il PC ha scelto: {pc.nome}")

    # Ciclo di 3 round
    for round in range(1, 4):
        print(f"\n--- ROUND {round} ---")
        giocatore.attacca(pc)
        if pc.numero_soldati <= 0:
            break  # Se il PC viene sconfitto, termina il ciclo
        pc.attacca(giocatore)
        print(f"Stato dopo round {round}:")
        print(giocatore)
        print(pc)

    # Mostra il risultato finale
    print("\n=== RISULTATO  ===")
    if giocatore.numero_soldati > pc.numero_soldati:
        print("HAI VINTO IL MATCH!")
    elif giocatore.numero_soldati < pc.numero_soldati:
        print("IL PC VINCE IL MATCH!")
    else:
        print("PAREGGIO!")


# ==========================
# AVVIO GIOCO
# ==========================

controllo = ControlloMilitare()  # Crea l'istanza del controllo militare per registrare unità
gioco()  # Avvia il gioco
