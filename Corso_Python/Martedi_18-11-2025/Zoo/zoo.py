# classe padre
class Animale: 
    # La classe base "Animale" attributi e metodi comuni a tutti gli animali

    def __init__(self, nome,eta):
        self.nome = nome
        self.eta = eta 

    def fai_suono(self):
        print(f"L'animale {self.nome} ha {self.eta} anni" )
        
        
# La classe "Leone" eredita da Animale e aggiunge ruggito  
class Leone(Animale):
    def __init__(self, nome, eta, ruggito):
        super().__init__(nome, eta)
        self.ruggito = ruggito

    def fai_suono(self):
        print(f"{self.nome} ruggisce: {self.ruggito}")

    def caccia(self):
        print(f"{self.nome} sta cacciando nella savana!")
        
        
# La classe "Giraffa" eredita da Animale e aggiunge altezza  

class Giraffa(Animale):
    def __init__(self, nome, eta, altezza):
        super().__init__(nome, eta)
        self.altezza = altezza

    def fai_suono(self):
        print(f"{self.nome} fa un suono da giraffa.")

    def mangia_foglie(self):
        print(f"{self.nome} sta mangiando foglie dagli alberi, altezza {self.altezza} m.")
        
        
# La classe "Pinguino" eredita da Animale e aggiunge specie  
class Pinguino(Animale):
    def __init__(self, nome, eta, specie):
        super().__init__(nome, eta)
        self.specie = specie

    def fai_suono(self):
        print(f"{self.nome} fa un suono da pinguino.")

    def nuota(self):
        print(f"{self.nome} sta nuotando")

leone1 = Leone("test", 5, "test") 
giraffa1 = Giraffa("test", 7, 8) 
pinguino1 = Pinguino("test", 2, "test") 

# --------------------multieriditarieta -------------------------
class Squalo(Animale,Pinguino):
    def __init__(self, nome, eta, specie):
        Animale.__init__(self,nome,eta)
        Pinguino.__init__(self,nome,eta,specie)
        
    def fai_suono(self):
        print(f"{self.nome} fa un suono da squalo!")
        
    def caccia(self):
        print(f"{self.nome} sta cacciando")
        
# eredita nuota() da pinguino



# richiamo i metodi che sovrascrivono quello del padre 
leone1.fai_suono()
giraffa1.fai_suono()
pinguino1.fai_suono()
#richiamo i metodi specifici
leone1.caccia()
giraffa1.mangia_foglie()
pinguino1.nuota()