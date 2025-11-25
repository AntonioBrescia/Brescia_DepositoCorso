from allenatore import Allenatore
from giocatore import Giocatore
from assistente import Assistente

def main():
    # Creazione dei membri del team
    allenatore = Allenatore("Mario Rossi", 50, 25)
    giocatore = Giocatore("Luca Bianchi", 24, "attaccante", 10)
    assistente = Assistente("Anna Verdi", 30, "preparazione atletica")
    
    # Interazioni
    print("=== Inizio allenamento ===")
    giocatore.descrivi()
    allenatore.dirige_allenamento()  # l'allenatore dirige l'allenamento
    giocatore.gioca_partita()        # il giocatore gioca una partita
    assistente.supporta_team()       # l'assistente supporta il team
    print("=== Fine allenamento ===")

main()
