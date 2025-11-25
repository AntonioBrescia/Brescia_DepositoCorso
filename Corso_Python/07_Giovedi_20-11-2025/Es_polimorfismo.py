class Animale:

    def emetti_suono(self):

        print("Questo animale fa un suono")


class Cane(Animale):

    def emetti_suono(self):

        print("Bau")


class Gatto(Animale):

    def emetti_suono(self):

        print("Miao")
        
        
#--------- SIMULAZIONE OVERLOADING ----------------------

class Stampa:

    def mostra(self, a=None, b=None):

        if a is not None and b is not None:

            print(a + b)

        elif a is not None:

            print(a)

        else:

            print("Niente da mostrare")

# -------------------duck typing POLIMORFISMO PASSIVO ---------------------
# 

class Cane:

    def parla(self):

        return "Bau!"


class Gatto:

    def parla(self):

        return "Miao!"
    
class Martello:

    def parla(self):

        return "Martello!"
    
    def balla(self):

        return "Martello!"


def fai_parlare(animale):

    # Non importa di che tipo sia l'animale,

    print(animale.parla())


cane = Cane()

gatto = Gatto()

martello = Martello()

#  IN BASE A COSA VIENE PASSATO NELLA FUNZIONE 
fai_parlare(cane)  # Output: Bau!

fai_parlare(gatto)  # Output: Miao!

fai_parlare(martello)  # Output: Bau!



# ----------- CICLO POLIMORFICO ------------
# E BUONA NORMA FARE UN CONTROLLO PRIMA, PER VERIFICARE SE L'OGGETTO GIUSTO 

class Cerchio:

    def disegna(self):

        print("Disegno un cerchio")


class Rettangolo:

    def disegna(self):

        print("Disegno un rettangolo")


def disegna_figura(figura):

    # Anche qui, basta che 'figura' abbia il metodo 'disegna'

    figura.disegna()


figure = [Cerchio(), Rettangolo()]     # figure[0]=Cerchio() / figure[1]=Rettagolo()


# Iteriamo e disegniamo ogni figura

for figura in figure:

    disegna_figura(figura)
    
    
    
# ESEMPIO CON len() di POLIMORFISMO 

# Lista

print(len([1, 2, 3]))  # Output: 3


# Stringa

print(len("Ciao"))     # Output: 4


# Dizionario

print(len({"a": 1, "b": 2}))  # Output: 2


# #Questa condizione verifica se il modulo viene eseguito direttamente
# (e non importato da un altro script). 
# Se è vero, allora il blocco di codice all’interno viene eseguito. 
# È una convenzione comune in Python per distinguere tra codice
# eseguibile direttamente e codice che viene importato come modulo.
# EVITIAMO DI AVERE PROBLEMI FUNZIONALI, SOLO SE RICHIAMATO POTRA PARTIRE 

if __name__ == "__main__":

    print("main")

else:

    print("import")