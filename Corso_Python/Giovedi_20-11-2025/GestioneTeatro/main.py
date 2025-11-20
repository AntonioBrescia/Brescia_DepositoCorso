from teatro import Teatro
from postoStandard import PostoStandard
from postoVip import PostoVIP

teatro = Teatro()

def menu_teatro():
    while True:
        print("\n--- MENU TEATRO ---")
        print("1 - Aggiungi posto Standard")
        print("2 - Aggiungi posto VIP")
        print("3 - Prenota un posto")
        print("4 - Stampa posti occupati")
        print("5 - Esci")

        scelta = input("Seleziona un'opzione: ")

        match scelta:
            case "1":
                numero = int(input("Numero posto: "))
                fila = input("Fila: ")
                costo = float(input("Costo prenotazione: "))
                teatro.aggiungi_posto(PostoStandard(numero, fila, costo))
                print(f"Posto Standard {fila}{numero} aggiunto.")

            case "2":
                numero = int(input("Numero posto: "))
                fila = input("Fila: ")
                servizi = input("Servizi extra separati da virgola: ").split(",")
                servizi = [s.strip() for s in servizi] 
                teatro.aggiungi_posto(PostoVIP(numero, fila, servizi))
                print(f"Posto VIP {fila}{numero} aggiunto.")

            case "3":
                numero = int(input("Numero posto da prenotare: "))
                fila = input("Fila: ")
                teatro.prenota_posto(numero, fila)

            case "4":
                teatro.stampa_posti_occupati()

            case "5":
                print("Exit")
                break

            case _:
                print("Scelta non valida. Riprova.")

if __name__ == "__main__":
    menu_teatro()
