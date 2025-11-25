import numpy as np

def creazione_salvataggio(file):
    nome_file = file
    arr_linspace = np.linspace(0, 10, 50)
    arr_random = np.random.random(50)
    somma_elementi = arr_linspace + arr_random

    # calcolo le somme 
    somma_totale = somma_elementi.sum()
    somma_maggiori_5 = somma_elementi[somma_elementi > 5].sum()
    
    # stampo risultati 
    print("array linspace: ", arr_linspace)
    print("-"*40)
    print("array casuale: ", arr_random)
    print("-"*40)
    print("array somma: ", somma_elementi)
    print("-"*40)
    print("somma totale: ", somma_totale)
    print("-"*40)
    print("somma elementi >5 : ", somma_maggiori_5)

    scelta= input(f"Vuoi sovrascrivere il file {nome_file}, premi 1 per sovrascrivere, 0 per non sovrascrivere? ")
    
    if scelta == "1":
        modalita = "w"
    else:
        modalita = "a"


    with open(nome_file, modalita) as f:
        f.write("Array linspace:\n" + np.array2string(arr_linspace) + "\n\n")
        f.write("Array casuale:\n" + np.array2string(arr_random) + "\n\n")
        f.write("Array somma:\n" + np.array2string(somma_elementi) + "\n\n")
        f.write(f"Somma totale: {somma_totale}\n")
        f.write(f"Somma elementi > 5: {somma_maggiori_5}\n")
        f.write("="*50 + "\n")


def main():
    while True:
        creazione_salvataggio("dati_array.txt")
        ripeti = input("Vuoi ripetere? (s/n): ").strip().lower()
        if ripeti != 's':
            print("Fine")
            break


if __name__ == "__main__":
    main()