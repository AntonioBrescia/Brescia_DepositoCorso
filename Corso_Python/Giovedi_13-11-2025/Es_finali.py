# ES 1 
print("Per sommare i numeri inseriti premi 0")

listaNumeri = []
somma = 0

numero = int(input("Inserisci il numero: "))

while numero != 0:
    listaNumeri.append(numero)
    somma += numero
    numero = int(input("Inserisci il numero: "))

print("Numeri inseriti:", listaNumeri)
print("Somma dei numeri:", somma)
print("---------------fine----------------")

print("---------------inizio es2----------------")
# ES 2
parola = input("Inserisci la parola: ")

for lettera in parola:
    print(lettera) 
# sulla stessa riga
parola = input("Inserisci la parola: ")
parola_stampata = "" 
for lettera in parola:
    parola_stampata += lettera 
print(parola_stampata)
print("---------------fine----------------")

print("---------------inizio es3----------------")

numeroMassimo = int(input("Inserisci il numero massimo: "))

step = int(input("Inserisci lo step: "))

for i in range(0, numeroMassimo + 1, step):
    print(i)
    
print("---------------fine----------------")
