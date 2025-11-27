import pandas as pd
import numpy as np

# Caricamento del dataset
df = pd.read_csv(r"Corso_Python\12_Giovedi_27-11-2025\Es_Az_Telecomunicazioni\dati.csv")

# ---------------------------
# Controllo valori mancanti
# ---------------------------
print("Valori mancanti per colonna ")
print(df.isnull().sum())

# Seleziona colonne numeriche da pulire
numerical_cols = ['Età', 'Durata_Abbonamento', 'Tariffa_Mensile', 'Dati_Consumati', 'Servizio_Clienti_Contatti']

# Riempie i valori mancanti con la mediana di ciascuna colonna
df[numerical_cols] = df[numerical_cols].fillna(df[numerical_cols].median())

# ---------------------------
# Correzione anomalie
# ---------------------------
df = df[(df['Età'] >= 18) & (df['Età'] <= 100)]
df = df[(df['Tariffa_Mensile'] >= 10) & (df['Tariffa_Mensile'] <= 100)]
df = df[(df['Dati_Consumati'] >= 0) & (df['Dati_Consumati'] <= 100)]
df = df[df['Servizio_Clienti_Contatti'] >= 0]

# Nuova colonna: Costo per GB
df['Costo_per_GB'] = df['Tariffa_Mensile'] / df['Dati_Consumati']

print(df[['Tariffa_Mensile', 'Dati_Consumati', 'Costo_per_GB']].head())
# Churn medio in base all'età
print(df.groupby('Età')['Churn'].value_counts(normalize=True).unstack().fillna(0))

# Tariffa media per Churn
print(df.groupby('Churn')['Tariffa_Mensile'].mean())

# Durata media dell'abbonamento in base alla Churn
print(df.groupby('Churn')['Durata_Abbonamento'].mean())
# Convertire Churn in 0 e 1 
df['Churn_num'] = df['Churn'].map({'No': 0, 'Sì': 1})

print(df[['Churn', 'Churn_num']].head())

df_normalized = df.copy()
for col in numerical_cols:
    min_val = np.min(df[col])
    max_val = np.max(df[col])
    df_normalized[col] = (df[col] - min_val) / (max_val - min_val)

print(df_normalized.head())

# Verifica 
print("Dataset pulito:")
print(df.info())
print(df.describe())
print(df['Churn'].value_counts())