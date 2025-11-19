class ContoBancario:
    def __init__(self, titolare, saldo_iniziale=0):
        # Attributi privati
        self.__titolare = None
        self.__saldo = 0
        # Imposta il titolare e il saldo iniziale tramite setter per validazione
        self.set_titolare(titolare)
        self.__saldo = saldo_iniziale
        
        
# METODI PUBBLICI 

    def deposita(self,importo):
        if importo > 0:
            self.__saldo += importo 
            print(f"Sono stati depositati {importo} sul tuo conto, il saldo attuale è {self.__saldo}")
        else:
            print(f"Importo non valido!")
    
    def preleva(self, importo):
        if importo > 0 and importo <= self.__saldo:
            self.__saldo -= importo
            print(f"Sono stati prelevati {importo} dal tuo conto, il saldo attuale è {self.__saldo}")
        else:
            print("Importo non valido!")
            
    def visualizza_saldo(self):
        return self.__saldo
    
    
    def get_titolare(self):
        return self.__titolare

    def set_titolare(self, nome):
        nome = str(nome).strip()  
        if nome:
            self.__titolare = nome
        else:
            print("Nome del titolare non valido")
            
            
            
            
def menu():
    while True:
        nome = input("Inserisci il nome del titolare: ")
        conto_temp = ContoBancario(nome)
        if conto_temp.get_titolare() is not None:
            conto = conto_temp
            break
        print("Riprova con un nome valido.")

    while True:
        print("\n--- MENU ---")
        print("1. Deposita")
        print("2. Preleva")
        print("3. Visualizza saldo")
        print("4. Esci")

        scelta = input("Scegli un'opzione (1-4): ")

        match scelta:
            case "1":
                importo = float(input("Inserisci importo da depositare: "))
                conto.deposita(importo)
            case "2":
                importo = float(input("Inserisci importo da prelevare: "))
                conto.preleva(importo)
            case "3":
                print(f"Saldo corrente: {conto.visualizza_saldo()}")
            case "4":
                print("Arrivederci.")
                break
            case _:
                print("Opzione non valida. Riprova.")

menu()
