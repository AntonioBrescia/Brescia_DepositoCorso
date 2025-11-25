import numpy as np
arr = np.linspace(0,1,10) #  Crea 5 numeri tra 0 e 1, distribuendoli in modo uguale.
print(arr)
random_arr = np.random.rand(3,3)
print(random_arr)

arr = np.array([1, 2, 3, 4, 5])


sum_value = np.sum(arr)

mean_value = np.mean(arr)

std_value = np.std(arr)


print("Sum:", sum_value)    # Output: Sum: 15

print("Mean:", mean_value)  # Output: Mean: 3.0

print("Standard Deviation:", std_value)  

# Output: Standard Deviation: 1.4142135623730951

# -------------------- Esercizio 1 ------------------------------
#  Crea 12 numeri tra 0 e 1
arr = np.linspace(0,1,12)


arr_reshape = arr.reshape(3, 4)

random_matrice = np.random.rand(3, 4)

somma_arr = arr_reshape.sum()
somma_random = random_matrice.sum()

print("Somma prima matrice:", somma_arr)
print("Somma matrice casuale:", somma_random)