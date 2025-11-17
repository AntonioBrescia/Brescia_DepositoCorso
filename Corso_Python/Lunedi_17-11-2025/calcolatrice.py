class Calcolatrice:
    @staticmethod
    def somma(a,b):
        return a + b
    
risultato = Calcolatrice.somma(5, 3)

print(risultato)

class Contatore: 
    numero_istanze = 0 
    
    def __init__(self):
        Contatore.numero_istanze += 1
        
    @classmethod
    def mostra_numero_istanze(cls):
        print(f"Sono state create {cls.numero_istanze} istanze.")
        
c1 = Contatore()
c2 = Contatore()
Contatore.mostra_numero_istanze()