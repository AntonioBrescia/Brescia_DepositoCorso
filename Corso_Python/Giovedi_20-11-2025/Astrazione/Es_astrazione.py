from abc import ABC, abstractmethod

class Animale(ABC):
    @abstractmethod
    def muovi(self):
        pass
class Cane(Animale):
    def muovi(self):
        print("corro")
        
class Pesce(Animale):
    def muovi(self):
        print("nuoto")
    
    
# Nell'esempio sopra, Animale è una classe astratta che
# definisce un metodo astratto muovi(). 
# Le classi Cane e Pesce sono classi concrete che ereditano
# da Animale e implementano il metodo muovi. Questo assicura
# che ogni sottoclasse di Animale abbia il proprio modo
# specifico di muoversi, ma dettagli come "come esattamente
# si muove un cane" sono astratti via.

#--------------------------------------------------------------------------------------------
class Lavoratore(ABC):
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

    @abstractmethod
    def calcola_stipendio(self):
        pass
    
class Impiegato(Lavoratore, ABC):
    def __init__(self, nome, cognome, stipendio_base):
        super().__init__(nome, cognome)
        self.stipendio_base = stipendio_base
    
    
class ImpiegatoFisso(Impiegato):
    def calcola_stipendio(self):
        return self.stipendio_base

class ImpiegatoAProvvigione(Impiegato):
    def __init__(self, nome, cognome, stipendio_base, vendite, percentuale):
        super().__init__(nome, cognome, stipendio_base)
        self.vendite = vendite
        self.percentuale = percentuale

    def calcola_stipendio(self):
        return self.stipendio_base + self.vendite * self.percentuale

    
def stampa_info_impiegati(lista_impiegati):
    for imp in lista_impiegati:
        print(f"{imp.nome} {imp.cognome} - Stipendio: {imp.calcola_stipendio()} €")
        
        
antonio = ImpiegatoFisso("Antonio", "Brescia", 2000)
giuseppe = ImpiegatoAProvvigione("Giuseppe", "Rossi", 1000, vendite=10000, percentuale=0.05)

lista = [antonio, giuseppe]

stampa_info_impiegati(lista)