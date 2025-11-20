class MetodoPagamento:
    nome = "Metodo di pagamento base"

    def effettua_pagamento(self, importo):
        return "Implemento nelle sotto classi il metodo"

class CartaDiCredito(MetodoPagamento):
    nome = "Carta di Credito"

    def effettua_pagamento(self, importo):
        print(f"Pagamento di {importo}€ con Carta di Credito")

class PayPal(MetodoPagamento):
    nome = "PayPal"

    def effettua_pagamento(self, importo):
        print(f"Pagamento di {importo}€ tramite PayPal")

class BonificoBancario(MetodoPagamento):
    nome = "Bonifico Bancario"

    def effettua_pagamento(self, importo):
        print(f"Pagamento di {importo}€ tramite Bonifico Bancario")


class GestorePagamenti:
    def __init__(self, metodo_pagamento):
        self.metodo = metodo_pagamento

    def paga(self, importo):
        self.metodo.effettua_pagamento(importo)
        print("Pagamento completato")


utenti = {}

def menu_pagamenti():
    nome_utente = input("Inserisci il tuo nome: ")
    if nome_utente not in utenti:
        utenti[nome_utente] = []

    while True:
        print("\nMenu:")
        print("1 - Aggiungi metodo di pagamento")
        print("2 - Effettua pagamento")
        print("3 - Mostra metodi registrati")
        print("4 - Esci")

        scelta = input("Scelta: ")

        match scelta:
            case "1":
                print("1 - Carta di Credito")
                print("2 - PayPal")
                print("3 - Bonifico Bancario")
                metodo_scelto = input("Seleziona metodo: ")
                match metodo_scelto:
                    case "1":
                        utenti[nome_utente].append(CartaDiCredito())
                        print("Carta di Credito aggiunta")
                    case "2":
                        utenti[nome_utente].append(PayPal())
                        print("PayPal aggiunto")
                    case "3":
                        utenti[nome_utente].append(BonificoBancario())
                        print("Bonifico Bancario aggiunto")
                    case _:
                        print("Metodo non valido")

            case "2":
                if not utenti[nome_utente]:
                    print("Nessun metodo registrato")
                    continue

                print("Seleziona metodo per pagare:")
                i = 1
                for m in utenti[nome_utente]:
                    print(f"{i}. {m.nome}")  
                    i += 1

                indice = int(input("Numero metodo: ")) - 1
                if 0 <= indice < len(utenti[nome_utente]):
                    importo = float(input("Importo da pagare: "))
                    gestore = GestorePagamenti(utenti[nome_utente][indice])
                    gestore.paga(importo)
                else:
                    print("Metodo non valido.")

            case "3":
                if utenti[nome_utente]:
                    print("Metodi registrati:")
                    for m in utenti[nome_utente]:
                        print("-", m.nome)  
                else:
                    print("Nessun metodo registrato.")

            case "4":
                print("Uscita.")
                break

            case _:
                print("Scelta non valida.")

menu_pagamenti()
