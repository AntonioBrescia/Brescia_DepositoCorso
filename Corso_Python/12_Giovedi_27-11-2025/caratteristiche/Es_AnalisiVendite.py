import pandas as pd
import numpy as np

# Creazione dati casuali
date = pd.date_range('2025-01-01', periods=31) 
citta = ['Bari', 'Milano', 'Torino']
prodotti = ['PC', 'Tastiera', 'Mouse']

# Creiamo il DataFrame con dati casuali
df = pd.DataFrame({
    'Data': np.random.choice(date, 31),
    'Città': np.random.choice(citta, 31),
    'Prodotto': np.random.choice(prodotti, 31),
    'Vendite': np.random.randint(50, 301, 31)  
})

print("DataFrame di esempio")
print(df)

# Pivot table: vendite medie per prodotto e città
pivot_df = df.pivot_table(values='Vendite', index='Prodotto', columns='Città', aggfunc='mean')
print("Vendite medie per prodotto e città")
print(pivot_df)

# GroupBy  vendite totali per prodotto
grouped_df = df.groupby('Prodotto')['Vendite'].sum()
print("Vendite totali per prodotto:")
print(grouped_df)
