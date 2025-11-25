studente = {
    "nome": "Alice",
    "eta" : 20,
    "sesso": "Femmina"
}

print(studente["nome"])
print(studente["eta"])
print(studente["sesso"])
studente["eta"] = 23

print(studente)

#Restituisce tutte le chiavi del dizionario.
print(studente.keys())
# Restituisce tutti i valori del dizionario.
print(studente.values())
# l metodo get() richiede almeno un argomento: la chiave da cercare. es studente.get("nome")
print(studente.get("nome"))

dizionario = {}

bool_input = input("Inserisci un valore booleano (True/False): ")

if bool_input.lower() == "true":
    bool_input = True
elif bool_input.lower() == "false":
    bool_input = False
else:
    print("Valore non valido, imposto False di default.")
    bool_input = False

intero_input = int(input("Inserisci un numero intero: "))
stringa_input = input("Inserisci una stringa: ")
lista_valori = [bool_input, intero_input, stringa_input]
dizionario["tipididato"] = lista_valori

dizionario2 = {
    "numero": intero_input,
    "booleano": bool_input,
    "stringa": stringa_input,
    "dizionari": lista_valori
}

for x ,y in dizionario2.items():
    print("chiave ",  x)
    print("valore ",  y)