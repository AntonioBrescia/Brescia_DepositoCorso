# gestore della matrice 2D
import numpy as np

# funzione di creazione della matrice 
def creazione():
    righe = int(input("Quante righe vuoi insirire? "))
    colonne = int(input("Quante colonne vuoi insirire? "))
    matrice = np.random.randint(1, 100, size=(righe, colonne))
    print("Matrice: ", matrice)
    salva_file("Matrice creata:\n" + str(matrice))
    return matrice
    
 # funzione di stampa sotto matrice     
def stampa_sottoMatrice(matrice):
    righe, colonne = matrice.shape

    if righe < 1 or colonne < 1:
        print("Matrice troppo piccola")
        return

    # Centro della matrice, prendo la parte intera della divisione 
    centro_r = righe // 2
    centro_c = colonne // 2

    # Determina il numero di righe e colonne da estrarre
    # Per righe
    if righe % 2 == 0:
        r_start = centro_r - 1
        r_end = centro_r + 1
    else:
        r_start = max(0, centro_r - 1)
        r_end = min(righe, centro_r + 2)

    # Per colonne
    if colonne % 2 == 0:
        c_start = centro_c - 1
        c_end = centro_c + 1
    else:
        c_start = max(0, centro_c - 1)
        c_end = min(colonne, centro_c + 2)

    sottomatrice = matrice[r_start:r_end, c_start:c_end]
    print(sottomatrice)
    salva_file("Sotto matrice centrale :\n" + str(sottomatrice))

    return sottomatrice

# funzione trasponi matrice 
def trasponi_matrice(matrice):
    trasposta = np.transpose(matrice)
    print(trasposta)
    salva_file("Matrice trasposta:\n" + str(trasposta))
    return trasposta

# funzione somma matrice 

def somma_elementi(matrice):
    somma_totale = np.sum(matrice)
    ris = f"la somma degli elementi è: {somma_totale}"
    salva_file(ris)
    return somma_totale

# funzione moltiplica matrice 

def moltiplica_matrici(matrice):
    righe, colonne = matrice.shape
    secondaMatrice = np.random.randint(1, 100, size=(righe, colonne))
    print("Seconda matrice:", secondaMatrice)
    
    risultato = matrice * secondaMatrice  
    print("Risultato delle moltiplicazioni tra matrici", risultato)
    ris = f"la moltiplicazione degli elementi è: {risultato}"
    salva_file(ris)
    return risultato

# funzione media matrice 

def media_elementi(matrice):
    media = np.mean(matrice)
    print("Media di tutti gli elementi: ", media)
    ris = f"la media  degli elementi è: {media}"
    salva_file(ris)

    return media

# funzione determinante matrice 

def determinante_matrice(matrice):
    righe, colonne = matrice.shape
    if righe != colonne:
        return None

    det = np.linalg.det(matrice)
    msg = f"Determinante della matrice: {det}"
    print(msg)
    salva_file(msg)
    return det

#funzione per salvare su file 
def salva_file(contenuto):
    with open("risultati_matrice.txt", "a") as f: 
        f.write(contenuto + "\n\n")

# menu 
def menu():
    matrice = None
    while True:
        print(".........Benvenuto.......")
        print("[1] Creare una nuova matrice")
        print("[2] Estrai e stampa la sotto-matrice")
        print("[3] Trasponi la matrice")
        print("[4] Calcola e stampa la somma di tutti gli elementi")
        print("[5] Crea e moltiplica con una seconda matrice")
        print("[6] Media degli elementi")    
        print("[7] Determinante della matrice ")
        print("[8] Esci")
        
        scelta = int(input("Scegli un'opzione: "))
        
        match scelta:
            case 1:
                matrice = creazione()
            case 2:
                if matrice is not None:
                    stampa_sottoMatrice(matrice)
                else:
                    print("Crea una matrice prima ")
            case 3:
                if matrice is not None:
                    matrice = trasponi_matrice(matrice)
                else:
                    print("Crea una matrice prima ")
            case 4:
                if matrice is not None:
                    somma_elementi(matrice)
                else:
                    print("Crea una matrice prima ")
            case 5:
                if matrice is not None:
                    moltiplica_matrici(matrice)
                else:
                    print("Crea una matrice prima ")
            case 6:
                if matrice is not None:
                    media_elementi(matrice)
                else:
                    print("Crea una matrice prima ")
            case 7:
                if matrice is not None:
                    determinante_matrice(matrice)
                else:
                    print("Crea una matrice prima ")
            case 8:
                print("ciao")
                break
            case _:
                print("comando non riconosciuto")

menu()
