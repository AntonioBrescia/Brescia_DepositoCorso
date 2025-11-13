numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nomi = ["Alice", "Bob", "Charlie"]
misto = [1, "due", True, 4.5]
# Stampa gli elementi delle liste
print("Numeri:", numeri)    
print("Nomi:", nomi)
print("Misto:", misto)
print(numeri[0])        # Primo elemento della lista numeri
print(numeri[2])        # Terzo elemento della lista numeri
print(nomi[1])         # Secondo elemento della lista nomi      
numeri[0]=100
print(numeri)
print(len(numeri))       # Lunghezza della lista numeri
#----------------------------------------------------------
numeri.append(11)      # Aggiunge 11 alla fine della lista numeri
print(numeri)
#----------------------------------------------------------
numeri.remove(5)      # Rimuove il numero 5 dalla lista numeri      
print(numeri)
#----------------------------------------------------------
numeri.insert(0, 0)   # Inserisce 0 all'inizio della lista numeri
print(numeri)       
#----------------------------------------------------------
numeri.sort()          # Ordina la lista numeri in ordine crescente
print(numeri)   
#----------------------------------------------------------
numeri.pop()            # Rimuove l'ultimo elemento della lista numeri
print(numeri)