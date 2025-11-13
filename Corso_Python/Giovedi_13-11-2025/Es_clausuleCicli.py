x = 22.4
print(type(x))

# La costante viene scritta in maiuscolo ma è solo una convezione. (In python non esistono le costanti)
COSTANTE = ""


# istruzione break ( interrompere l'esecuzione di un ciclo)
numeri = [1,2,3,4,5]
for numero in numeri:
    if numero == 3:
        break
    print(numero)
    
# istruzione continue ( salta l'esecuzione di un ciclo in questo caso il 3)
for numero in numeri:
    if numero == 3:
        continue
    print(numero)
    
print("-----------------------------------")

for i in range(5):
    if i == 3:
        pass
    print(i)

# operatore splat 
# serve a creare una lista, tupla ecc.. in questo es crea una lista da 1 a 10 
numeri = [*range(1,11)]
print(numeri)