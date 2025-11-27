import pandas as pd
import numpy as np

file_path = r"Corso_Python\12_Giovedi_27-11-2025\Prove_pandas\vendite.csv"


# Caricamento dei dati nel DataFrame
# in genere si mette df_vendite = ....
df = pd.read_csv(file_path)

#le prime righe del DataFrame per confermare 
# dentro le parantesi puoi mettere quante righe vuoi estrarre 
print(df.head(2))

# Creazione di un DataFrame con dati di esempio

data = {

    'Nome': ['Alice', 'Bob', 'Carla'],

    'Età': [25, 30, 22],

    'Città': ['Roma', 'Milano', 'Napoli']

}

df = pd.DataFrame(data)


# Stampa del DataFrame originale

print("DataFrame Originale:")

print(df)


# Selezione delle righe dove l'età è superiore a 23

df_older = df[df['Età'] > 23]


# Stampa delle righe selezionate

print("\nPersone con età superiore a 23 anni:")

print(df_older)


# Aggiungiamo una nuova colonna  la persona maggiorenne

df['Maggiorenne'] = df['Età'] >= 18


# Stampa del DataFrame con la nuova colonna

print("\nDataFrame con colonna 'Maggiorenne':")

print(df)



# DataFrame esempio, inclusi valori mancanti e duplicati

data = {

    'Nome': ['Alice', 'Bob', 'Carla', 'Bob', 'Carla', 'Alice', None],

    'Età': [25, 30, 22, 30, np.nan, 25, 29],

    'Città': ['Roma', 'Milano', 'Napoli', 'Milano', 'Napoli', 'Roma', 'Roma']

}

df = pd.DataFrame(data)


# Stampa del DataFrame originale

print("DataFrame Originale:")

print(df)


# Rimozione dei duplicati

df = df.drop_duplicates()


# Gestione dei dati mancanti

# Rimozione delle righe dove almeno un elemento è mancante

df_cleaned = df.dropna()


# possiamo sostituire dati mancanti con valore di default

df['Age'].fillna(df['Age'].mean(), inplace=True)

def classifica_eta(eta):
    if eta <= 18:
        return "Giovane"
    elif eta <= 65:
        return "Adulto"
    else:
        return "Senior"

print(df.columns)
# Applicare la funzione alla colonna Età
df["Categoria Età"] = df["Age"].apply(classifica_eta)

# Visualizzare alcune righe per controllo
print("DataFrame con nuova colonna 'Categoria Età':")
print(df[['Age', 'Categoria Età']].head(10))
print("-" * 60)


# Stampa del DataFrame pulito

print("\nDataFrame dopo la pulizia:")

print(df_cleaned)


# Stampa del DataFrame con dati mancanti sostituiti

print("\nDataFrame con dati mancanti sostituiti:")

print(df)