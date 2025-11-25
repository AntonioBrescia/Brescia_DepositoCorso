from libro import Libro

class Biblioteca:
    def __init__(self):
        self.libri = []

    def aggiungi_libro(self, libro):
        self.libri.append(libro)

    def stampa_libri(self):
        if len(self.libri) == 0:
            print("La biblioteca è vuota")
        else:
            for libro in self.libri:
                print(libro)

biblioteca = Biblioteca()


while True:
    print("Inserisci i dati del libro (o 'stop' per terminare):")
    titolo = input("Titolo: ")
    if titolo.lower() == 'stop':
        break
    autore = input("Autore: ")
    pagine = int(input("Numero di pagine: "))  

    libro = Libro(titolo, autore, pagine)
    biblioteca.aggiungi_libro(libro)
    print(f"Libro '{titolo}' aggiunto con successo!")
    
    
print("Ecco i libri presenti nella biblioteca:")
biblioteca.stampa_libri()
