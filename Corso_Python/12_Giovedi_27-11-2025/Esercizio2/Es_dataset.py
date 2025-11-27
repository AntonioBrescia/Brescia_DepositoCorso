import pandas as pd
import numpy as np


file_path = 'Corso_Python/12_Giovedi_27-11-2025/Esercizio2/prodotti.csv'

df = pd.read_csv(file_path)

df['Totale Vendite'] = df['quantita'] * df['prezzo_unitario']
print(df)

# Raggruppare per prodotto e sommare il totale vendite
# Raggruppa il DataFrame df in base ai valori della colonna prodotto.
# .sum() → somma dei valori numerici nei gruppi
# reset_index() Trasforma l’indice (prodotto) in colonna normale
totale_per_prodotto = df.groupby('prodotto')['Totale Vendite'].sum().reset_index()

# Ordina dal totale più alto al più basso 
totale_per_prodotto = totale_per_prodotto.sort_values(by='Totale Vendite', ascending=False)

print(totale_per_prodotto)

""" # df.groupby('prodotto')['quantita'].sum()  somma la quantità di ogni prodotto.

.reset_index()  trasforma l’indice prodotto in colonna normale.

.sort_values(by='quantita', ascending=False) ordina dal prodotto con più quantità a quello con meno.

.iloc[0]  prende la prima riga il prodotto con più vendite in quantità. """

quantita_per_prodotto = df.groupby('prodotto')['quantita'].sum().reset_index()

# ordina per quantità decrescente e prendere il primo prodotto
prodotto_piu_venduto = quantita_per_prodotto.sort_values(by='quantita', ascending=False).iloc[0]

print("Prodotto più venduto in termini di quantità:")
print(prodotto_piu_venduto)

vendite_per_citta = df.groupby('citta')['Totale Vendite'].sum().reset_index()

prima_citta = vendite_per_citta.sort_values(by='Totale Vendite', ascending=False).iloc[0]

print("Città con il maggior volume di vendite totali:")
print(prima_citta)
# Valore soglia
df['Totale Vendite'] = df['Totale Vendite'].astype(float)
soglia = int(input("Quale valore vuoi inserire? "))

# Creare un nuovo DataFrame filtrato
vendite_grandi = df[df['Totale Vendite'] > soglia]

# Controllare il risultato
print(vendite_grandi)
file_pathVendite = 'Corso_Python/12_Giovedi_27-11-2025/Esercizio2/topVendite.csv'

vendite_grandi.to_csv(file_pathVendite, index=False)


# Ordino il DataFrame per Totale Vendite in ordine decrescente
df_ordinato = df.sort_values(by='Totale Vendite', ascending=False)

# Controllare il risultato
print(df_ordinato)