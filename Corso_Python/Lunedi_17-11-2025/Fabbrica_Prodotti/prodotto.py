class Prodotto:
    def __init__(self, nome, costo_produzione, prezzo_vendita):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita

    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione

class Elettronica:
    def __init__(self, nome, costo_produzione, prezzo_vendita, garanzia):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
        self.garanzia = garanzia

    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione

class Abbigliamento:
    def __init__(self, nome, costo_produzione, prezzo_vendita, materiale):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
        self.materiale = materiale

    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione
    
class Fabbrica:
    def __init__(self):
        # chiave = nome del prodotto
        # valore = dizionario con 'prodotto' e 'quantita'
        self.inventario = {}

    def aggiungi_prodotto(self, prodotto, quantita):
        if prodotto.nome in self.inventario:
            self.inventario[prodotto.nome]['quantita'] += quantita
        else:
            self.inventario[prodotto.nome] = {'prodotto': prodotto, 'quantita': quantita}
        print(f"Aggiunti {quantita} pezzi di {prodotto.nome} all'inventario")

    def vendi_prodotto(self, nome, quantita):
        if nome in self.inventario and self.inventario[nome]['quantita'] >= quantita:
            self.inventario[nome]['quantita'] -= quantita
            prodotto = self.inventario[nome]['prodotto']
            profitto = prodotto.calcola_profitto() * quantita
            print(f"Venduti {quantita} pezzi di {nome}. Profitto realizzato: {profitto}")
        else:
            print(f"Prodotto {nome} non disponibile o quantità insufficiente")

    def resi_prodotto(self, prodotto, quantita):
        if prodotto.nome in self.inventario:
            self.inventario[prodotto.nome]['quantita'] += quantita
        else:
            self.inventario[prodotto.nome] = {'prodotto': prodotto, 'quantita': quantita}
        print(f"Aggiunti {quantita} pezzi di {prodotto.nome} come reso")



# ------------------------------------------Creazione e test-------------------------------------
# Creazione prodotti

maglietta = Abbigliamento("Maglietta", 10, 25, "Cotone")
telefono = Elettronica("Smartphone", 200, 350, "2 anni")

# Creazione fabbrica
fabbrica = Fabbrica()

# Aggiungi prodotti all'inventario
fabbrica.aggiungi_prodotto(maglietta, 50)
fabbrica.aggiungi_prodotto(telefono, 20)

# Vendi prodotti
fabbrica.vendi_prodotto("Maglietta", 10)
fabbrica.vendi_prodotto("Smartphone", 5)

# Resi prodotti
fabbrica.resi_prodotto(maglietta, 2)


