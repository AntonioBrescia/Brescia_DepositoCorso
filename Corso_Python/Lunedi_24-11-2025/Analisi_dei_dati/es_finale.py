import numpy as np

# creo un array da 0 a 49
array_1 = np.arange(50)

# array con 50 valori casuali tra 49 e 101 
array_2 = np.random.randint(49, 101, size=50)

# concateno i due array 
array_finale = np.concatenate((array_1, array_2))

# stampo array, dtype e shape
print("Array finale: ", array_finale)
print("Tipo di dato :", array_finale.dtype)
print("Shape dell'array:", array_finale.shape)

# modifico il tipo di dato in float64
array_float = array_finale.astype(np.float64)

# primi 10 elementi 
primi_10 = array_finale[:10]
print("Primi 10 elementi:", primi_10)

# ultimi 7 
ultimi_7 = array_finale[-7:]
print("Ultimi 7:", ultimi_7)

# dall'indice 5 a indice 20 escluso
da_5_20 = array_finale[5:20]
print("Elementi dall'indice 5 a 20:", da_5_20)

# ogni quarto elemento (correzione del tuo errore)
ogni_quattro = array_finale[::4]
print("Ogni quarto elemento:", ogni_quattro)

# modifico gli elementi dall'indice 10 all'indice 15 assegnando 999
array_finale[10:15] = 999
print("Array modificato: ", array_finale)

# elementi in det posizioni
posizioni = [0, 3, 7, 12, 25, 33, 48]
fancy_posizioni = array_finale[posizioni]

# elementi pari con maschera booleana
elementi_pari = array_finale[array_finale % 2 == 0]

# elementi maggiori della media
media = array_finale.mean()
maggiori_media = array_finale[array_finale > media]

# Stampa risultati
print("ARRAY FINALE DOPO MODIFICHE:", array_finale)

print("Sotto-array modificato (indici 10-15):", array_finale[10:15])

print("Fancy indexing:", fancy_posizioni)

print("Elementi pari dell’array:", elementi_pari)

print("Elementi maggiori della media:", maggiori_media)

print("Media dell’array:", media)
