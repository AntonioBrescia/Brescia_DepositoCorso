import numpy as np
# Creazione di un array unidimensionale

arr = np.array([1, 2, 3, 4, 5])


# Creazione di un array bidimensionale
arr2d = np.array([[1, 2, 3], [4, 5, 6]])

# ndarray → struttura principale di NumPy: array multidimensionale

# dtype → tipo di dato contenuto nell'array (int32, float64, ecc.)

# shape → forma dell'array: numero di righe, colonne, dimensioni

# arange → crea una sequenza di valori con passo definito (come range)

# reshape → cambia la forma dell'array senza modificarne i valori

# linspace → crea valori equidistanti specificando quanti generarne

# random → genera numeri casuali (interi, float, matrici casuali)

# sum → somma tutti gli elementi (o lungo un asse)

# mean → calcola la media

# std → calcola la deviazione standard

arr = np.array([1, 2, 3])
print(arr.dtype) 
arr = np.array([1, 2, 3, 4])

print(np.std(arr))

# Creazione di un array

arr = np.array([1, 2, 3, 4, 5])
a = np.zeros(10)
print(a)
b = [0,0,0,0,0,0,0,0,0]
print("b: " , b)
# Utilizzo di alcuni metodi

print("Forma dell'array:", arr.shape)  # Output: (5,)

print("Dimensioni dell'array:", arr.ndim)  # Output: 1

print("Tipo di dati:", arr.dtype)  # Output: int64 (varia a seconda della piattaforma)

print("Numero di elementi:", arr.size)  # Output: 5

print("Somma degli elementi:", arr.sum())  # Output: 15

print("Media degli elementi:", arr.mean())  # Output: 3.0

print("Valore massimo:", arr.max())  # Output: 5

print("Indice del valore massimo:", arr.argmax())  # Output: 4

# Creazione di un array unidimensionale
# Creazione di un array unidimensionale

arr = np.array([1, 2, 3], dtype='int32')

print(arr.dtype)  # Output: int32

# Creazione di un array bidimensionale

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr.shape)  # Output: (2, 3)

arr = np.arange(10)

print(arr)  # Output: [0 1 2 3 4 5 6 7 8 9]

arr = np.arange(6)

reshaped_arr = arr.reshape((2, 3))

print(reshaped_arr)

# Output:  [[0 1 2] [3 4 5]]



#----------------------------------- INIZIO ESERCIZIO --------------------------------------

print("----------------------------------- INIZIO ESERCIZIO --------------------------------------")
# array di numeri interi da 10 a 49
array = np.arange(10, 50)
print("Array originale:", array)

#  tipo di dato (dtype)
print("Tipo di dato originale:", array.dtype)

array = np.arange(10, 50, dtype=np.float64)

# cambio tipo di dato in float64
print("Array in float:", array)
print("Tipo di dato dopo la conversione:", array.dtype)

# forma dell'array
print("Forma dell'array:", array.shape)

arr = np.arange(12)
arr_reshaped = arr.reshape(3, 4)

arr = np.array([0, 2, 0, 5])
print(arr.nonzero()) # restituisce gli indici degli elementi diversi da zero.
arr.reshape(3, 4)

#  -----------------------------------------------------------------------

arr = np.array([1, 2, 3, 4, 5])

print(arr[0])  # Output: 1

print(arr[1:3])  # Output: [2 3]

print(arr[arr > 2])  # Output: [3 4 5]

arr_2d = np.array([[1, 2, 3, 4],

                   [5, 6, 7, 8],

                   [9, 10, 11, 12]])

# Slicing sulle righe

print(arr_2d[1:3])  

# Slicing sulle colonne

print(arr_2d[:, 1:3])  

# Slicing misto

print(arr_2d[1:, 1:3])  

# ------------------ ESEMPI DI SLICING -----------------------

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


# Slicing di base

print(arr[2:7])  # Output: [2 3 4 5 6]


# Slicing con passo

print(arr[1:8:2])  # Output: [1 3 5 7]


# Omettere start e stop

print(arr[:5])  # Output: [0 1 2 3 4]

print(arr[5:])  # Output: [5 6 7 8 9]


# Utilizzare indici negativi

print(arr[-5:])  # Output: [5 6 7 8 9]

print(arr[:-5])  # Output: [0 1 2 3 4]

arr = np.array([10, 20, 30, 40, 50])


# Utilizzo di un array di indici
arr = np.array([10, 20, 30, 40, 50])


# Utilizzo di un array di indici

indices = np.array([1, 3])

print(arr[indices])  # Output: [20 40]


# Utilizzo di una lista di indici

indices = [0, 2, 4]

print(arr[indices])  # Output: [10 30 50]