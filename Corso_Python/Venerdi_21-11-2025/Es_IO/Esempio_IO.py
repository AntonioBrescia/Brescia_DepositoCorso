# Apertura del file in lettura
# I O funzione open() per aprire il file accetta due parametri il path e la modalita r intesa come read
file = open("Corso_Python\\Venerdi_21-11-2025\\Es_IO\\test.txt", "r")

contenuto = file.read()
file.close()

# Stampa il contenuto letto
print(contenuto)

# Apertura del file in scrittura (sovrascrive il contenuto)
file = open("Corso_Python\\Venerdi_21-11-2025\\Es_IO\\test.txt", "w")

file.write("Questo è un esempio di scrittura sul file ")
file.close()

# possiamo utilizzare with che si occupa automaticamente della chiusura del file 

with open("Corso_Python\\Venerdi_21-11-2025\\Es_IO\\test.txt", "r") as file:
    contenuto2 = file.read()
    print("Questo è il contenuto 2", contenuto2)