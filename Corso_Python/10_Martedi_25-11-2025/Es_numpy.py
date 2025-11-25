# somma e media degli elementi 
import numpy as np

# Creare un array di 15 elementi con numeri casuali tra 1 e 100
array = np.random.randint(1, 101, size=15)  
# stampo l'array 
print("Array:", array)

# Calcolare e stampare la somma degli elementi
somma = np.sum(array)
print("Somma degli elementi:", somma)

# Calcolare e stampare la media degli elementi
media = np.mean(array)
print("Media degli elementi:", media)


#-----------------  ESERCIZIO 2 --------------------------------------------------------
# Creare una matrice 5x5 con numeri sequenziali da 1 a 25
matrice = np.arange(1, 26).reshape(5, 5)
print("Matrice 5x5:", matrice)

# stampo la seconda colonna 
seconda_colonna = matrice[:, 1]
print("Seconda colonna:", seconda_colonna)

# stampo la terza riga 
terza_riga = matrice[2, :]
print("Terza riga:", terza_riga)

diagonale = np.diag(matrice)

# calcolo somma della diagonale 
somma_diagonale = np.sum(diagonale)
print("Somma della diagonale:", somma_diagonale)


#------------------ ESERCIZIO 3 ------------------------------------------------------


# array 4x4 con numeri casuali tra 10  50
array = np.random.randint(10, 51, size=(4, 4))
print("Array originale:\n", array)

# elementi agli indici specificati 
righe = np.array([0, 1, 2, 3])
colonne = np.array([1, 3, 2, 0])
elementi_selezionati = array[righe, colonne]
print("Elementi selezionati:", elementi_selezionati)

# Selezionare tutte le righe dispari 
righe_dispari = array[1::2, :]  
print("Righe dispari:", righe_dispari)

# Aggiungo 10 agli elementi 
array[righe, colonne] += 10
print("Array dopo modifica:", array)
