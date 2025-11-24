import numpy as np
# array con numeri casuali tra 10 e 50 
arr = np.random.randint(10,51, size=20)
print("Array di partenza:", arr)

# primi 10 
primi_10 = arr[:10]
print("Primi 10 elementi:", primi_10)

# ultimi 5 
ultimi_5 = arr[-5:]
print("Ultimi 5:", ultimi_5)

# dall inidice 5 a indice 15
da_5_15 = arr[5:15]
print("Elementi dall'indice 5 a 15:", da_5_15)

# ogni terzo elemento 
ogni_terzo = arr[::3]
print("Ogni terzo elemento:", ogni_terzo)

# modifico gli elementi dall' indice 5 all' indice 10 assegnando 99
arr[5:10] = 99
print("Array modificato: ", arr)

# ---------- CON MATRICE  ----------------------------------

# matrice 4x5 con numeri tra 10 e 50
matrice = np.random.randint(10, 51, size=(4,5))
print("Matrice iniziale :", matrice)

# prime 2 righe
prime_2_righe = matrice[:2, :]
print("Prime 2 righe:", prime_2_righe)

# ultime due colonne 
ultime_2_colonne = matrice[:, -2:]
print("Ultime 2 colonne: ", ultime_2_colonne)




#--------------- ES 2 -----------------------

# Creo matrice 6x6 con numeri interi casuali tra 1 e 100
matrice = np.random.randint(1, 101, size=(6, 6))
print("Matrice originale: ", matrice)

# Estrarre la sotto-matrice 4x4
sotto_matrice = matrice[1:5, 1:5]
print("Sotto matrice centrale 4x4: ", sotto_matrice)

# inverto le righe della sotto matrice 
matrice_invertita = sotto_matrice[::-1, :]
print("Sotto matrice con righe invertite: ", matrice_invertita)

# diagonale principale della matrice invertita
diagonale = np.diag(matrice_invertita)
print("Diagonale principale: ", diagonale)

# sostituire tutti gli elementi multipli di 3 con -1
matrice_modificata = matrice_invertita.copy()
matrice_modificata[matrice_modificata % 3 == 0] = -1