class Libreria:
    def __init__(self):
        self.catalogo = []

    def aggiungi_libro(self, isbn, titolo, autore):
        self.catalogo.append([isbn, [titolo, autore]])

    def rimuovi_libro(self, isbn):
        for libro in self.catalogo:
            if libro[0] == isbn:
                self.catalogo.remove(libro)
                return True
        return False

    def mostra_catalogo(self):
        if not self.catalogo:
            print("Il catalogo è vuoto.")
        else:
            for libro in self.catalogo:
                print(f"ISBN: {libro[0]}, Titolo: {libro[1][0]}, Autore: {libro[1][1]}")
                
                
    def cerca_per_titolo(self, titolo):
        trovati = []  
        for libro in self.catalogo:
            if libro[1][0] == titolo:
                trovati.append(libro)
        
        if trovati:
            for libro in trovati:
                print(f"ISBN: {libro[0]}, Titolo: {libro[1][0]}, Autore: {libro[1][1]}")
        else:
            print(f"Nessun libro trovato con il titolo '{titolo}'")
