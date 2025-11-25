class Libro:
    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
        
    def descrizione(self):
        return f"Il libro {self.titolo} è stato scritto da {self.autore} e ha {self.pagine} pagine"
    
    def __str__(self):
        return self.descrizione()