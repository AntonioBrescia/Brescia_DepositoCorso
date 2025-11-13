# tipo int (numeri interi positivi o negativi)
x = 10 
y = -2
print(x , y)

# SI USA IL PUNTO NON LA VIRGOLA PER I NUMERI DECIMALI
# tipo float (numeri con la virgola positivi o negativi)
a = 3.14
b = -0.5    
print(a , b)

# tipo str (stringhe di testo)
saluto = "Ciao"
nome = "Antonio"      
cognome = 'Brescia'
messaggio = saluto + ", " + nome + " " + cognome + "!"
print(messaggio)

z = "10"  
print(z[0])  # stampa il primo carattere della stringa '10'

s = "Ciao, mondo!"
print(len(s))  # stampa la lunghezza della stringa
print(s.lower())  # stampa la stringa in minuscolo
print(s.upper())  # stampa la stringa in maiuscolo  
print(s.replace("mondo", "Universo"))  # sostituisce "Ciao" con "Ciao"
print(s.split(","))  # divide la stringa in una lista usando la virgola come separatore

carattere = 'A' # tipo char (singolo carattere)
print(carattere)  

a = True   # tipo bool (booleano)
b = False                       
print(a , b)
# Operatori aritmetici        
x = 5 
y = 10
z = 7
print(x < y and y > z)  # True
print(x < y or y > z)   # True
print(not(x < y))       # False

# Operatori di confronto
print(x == y)  # False
print(x != y)  # True       
print(x < y)  # True    
print(x <= y) # True
print(x > y)  # False


