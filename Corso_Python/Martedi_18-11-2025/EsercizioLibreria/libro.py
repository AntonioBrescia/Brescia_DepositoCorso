class Libro:
    def __init__(self, titolo,autore,isbn):
        self.titolo = titolo
        self.autore = autore
        self.isbn = isbn
        

    def descrizione(self):
        return f"Titolo: {self.titolo}, Autore: {self.autore}, ISBN: {self.isbn}"