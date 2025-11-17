class Libro:
    def __init__ (self,titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
        
    def descrizione(self):
        return f"Il libro {self.titolo} è stato scritto da {self.autore} e ha {self.pagine} pagine"
    
    def __str__(self):
        return self.descrizione()

libri = []
libro1 = Libro("Divina Commedia", "Dante", 500)
libro2 = Libro("TEST", "TEST", 500)
libri.append(libro1)
libri.append(libro2)

for libro in libri:
    print(libro)
    
    
#print(libro1.descrizione())
