import pandas as pd

data = {
    'Data': ['2021-01-01', '2021-01-01', '2021-01-01', '2021-01-02', '2021-01-02'],
    'Città': ['Roma', 'Milano', 'Napoli', 'Roma', 'Milano'],
    'Prodotto': ['Mouse', 'Tastiera', 'Mouse', 'Tastiera', 'Mouse'],
    'Vendite': [100, 200, 150, 300, 250]
}

df = pd.DataFrame(data)

# Convertire in datetime
df['Data'] = pd.to_datetime(df['Data'])

# Impostare indice datetime
df.set_index('Data', inplace=True)

# Resample solo sulle colonne numeriche
df_daily = df['Vendite'].resample('D').mean()
df_monthly = df['Vendite'].resample('M').sum()

print("Media giornaliera:")
print(df_daily, "\n")

print("Totale mensile:")
print(df_monthly)


# series.shift() Sposta i valori lungo l'asse temporale 
# aggiunge una colonna con il valore del giorno precedente

df['prev_day'] = df['value'].shift(1)

# tasso di variazione giornaliero

df['daily_return'] = df['value'].pct_change()  

# equivalente a shift + calcolo %
# finestra mobile di 7 giorni: media e deviazione standard

df['rolling_mean7'] = df['value'].rolling(window=7).mean()

df['rolling_std7']  = df['value'].rolling(window=7).std()