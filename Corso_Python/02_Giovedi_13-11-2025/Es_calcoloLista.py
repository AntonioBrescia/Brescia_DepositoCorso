fattori = []

valore1 = float(input("Inserisci il primo valore: "))
fattori.append(valore1)

valore2 = float(input("Inserisci il secondo valore: "))
fattori.append(valore2)

valore3 = float(input("Inserisci il terzo valore: "))
fattori.append(valore3)

operazione = input("Scegli 1 per sommare o 2 per sottrarre gli elementi: ")

if operazione == "1":
    risultato = sum(fattori)
    print("La somma dei valori è:", risultato)
elif operazione == "2":
    risultato = fattori[0] - fattori[1] - fattori[2]
    print("La sottrazione dei valori è:", risultato)
else:
    print("Scelta non valida.")
