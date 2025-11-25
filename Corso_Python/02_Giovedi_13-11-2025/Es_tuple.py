# Es tuple
punto = (3, 4)
colore_rgb = (255,128,0)
informazioni_persona = ("alice", 25, "Femmina")

print(punto[0])
print(punto[1])

punto = 3, 4
x, y = punto
print(x)

#Insiemi 
set1 = set([1,2,3,4,5])
set2 = {4,5,6,7,8}
#---------------------
print(set1)
#---------------------
print(set2)
#---------------------
# output union {1, 2, 3, 4, 5, 6, 7, 8}
print(set1.union(set2))
#---------------------
# output intersection {4, 5}
print(set1.intersection(set2))
#---------------------
# output difference {1, 2, 3}
print(set1.difference(set2))
#---------------------
# output symmetric_difference {1, 2, 3, 6, 7, 8}
print(set1.symmetric_difference(set2))

# METODI PER L'INSIEMI 
set2.add(10)
print(set2)
set2.remove(10)
print(set2)
set2.discard(10)
print(set2)
print("stampo la lunghezza")
print(len(set2))

copia_set1 = set1.copy()
colori = {"rosso", "verde", "blu"}

colore = input("Inserisci un colore: ")
if colore in colori:
    print("Colore disponibile!")
else:
    print("Colore non disponibile.")
