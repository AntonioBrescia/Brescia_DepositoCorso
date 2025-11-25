from gestoreParco import GestoreParcoVeicoli
from auto import Auto
from furgone import Furgone
from motocicletta import Motocicletta


def menu():
    gestore = GestoreParcoVeicoli()

    while True:
        print("===== MENU PARCO VEICOLI =====")
        print("1. Aggiungi veicolo")
        print("2. Rimuovi veicolo")
        print("3. Lista veicoli")
        print("4. Operazioni su un veicolo")
        print("0. Esci")
        
        scelta = input("Scegli un'opzione: ")

        match scelta:
            case "1":
                print("--- Aggiungi Veicolo ---")
                tipo = input("Tipo (auto / furgone / moto): ").lower()
                marca = input("Marca: ")
                modello = input("Modello: ")
                anno = int(input("Anno: "))

                match tipo:
                    case "auto":
                        porte = int(input("Numero porte: "))
                        veicolo = Auto(marca, modello, anno, porte)

                    case "furgone":
                        capacita = int(input("Capacità carico (kg): "))
                        veicolo = Furgone(marca, modello, anno, capacita)

                    case "moto":
                        tipo_moto = input("Tipo (sportiva/touring/...): ")
                        veicolo = Motocicletta(marca, modello, anno, tipo_moto)

                    case _:
                        print("Tipo non valido.")
                        continue

                gestore.aggiungi_veicolo(veicolo)

            case "2":
                print("--- Rimuovi Veicolo ---")
                marca = input("Marca: ")
                modello = input("Modello: ")
                gestore.rimuovi_veicolo(marca, modello)

            case "3":
                print("--- Lista Veicoli ---")
                gestore.lista_veicoli()

            case "4":
                print("--- Operazioni su Veicolo ---")
                marca = input("Marca: ")
                modello = input("Modello: ")

                veicolo = None
                for v in gestore._veicoli:
                    if v._marca == marca and v._modello == modello:
                        veicolo = v
                        break

                if veicolo is None:
                    print("Veicolo non trovato!")
                    continue

                print(f"Veicolo selezionato: {veicolo}")

                print("1. Accendi")
                print("2. Spegni")
                print("3. Operazione speciale")

                op = input("Scegli un'operazione: ")

                match op:
                    case "1":
                        veicolo.accendi()
                    case "2":
                        veicolo.spegni()
                    case "3":
                        match veicolo:
                            case Auto():
                                veicolo.suona_clacson()
                            case Motocicletta():
                                veicolo.esegui_wheelie()
                            case Furgone():
                                carScar = input("Caricare o scaricare? (c/s): ").lower()
                                if carScar == "c":
                                    q = int(input("Quantità da caricare: "))
                                    veicolo.carica(q)
                                elif carScar == "s":
                                    q = int(input("Quantità da scaricare: "))
                                    veicolo.scarica(q)
                                else:
                                    print("Scelta non valida.")
                    case _:
                        print("Operazione non valida.")

            case "0":
                print("Uscita dal programma...")
                break

            case _:
                print("Scelta non valida! Riprova.")

    
    
menu()
