import pandas as pd
import numpy as np

#  DataFrame 

file_path = r"Corso_Python\12_Giovedi_27-11-2025\Esercizio1\utenti.csv"
df = pd.read_csv(file_path)
print(df)

#  Rimozione duplicati
df = df.drop_duplicates()

# Gestione valori mancanti
# valori mancanti nella colonna Età e Salario con la mediana
df['Età'] = df['Età'].fillna(df['Età'].median())
df['Salario'] = df['Salario'].fillna(df['Salario'].median())

# Creazione colonna Categoria Età
def classifica_eta(eta):
    if eta <= 18:
        return "Giovane"
    elif eta <= 65:
        return "Adulto"
    else:
        return "Senior"

df['Categoria Età'] = df['Età'].apply(classifica_eta)

# Statistiche descrittive sulle colonne numeriche
print("\nStatistiche descrittive (solo colonne numeriche):")
print("Media:\n", df.mean(numeric_only=True))
print("Mediana:\n", df.median(numeric_only=True))
print("Deviazione standard:\n", df.std(numeric_only=True))

# Stampa del DataFrame pulito
print("DataFrame pulito con colonna Categoria Età")
print(df)

# Salvo in CSV
output_file = r"Corso_Python\12_Giovedi_27-11-2025\Esercizio1\vendite_clean.csv"
df.to_csv(output_file, index=False)
print(f"DataFrame pulito salvato in: {output_file}")
